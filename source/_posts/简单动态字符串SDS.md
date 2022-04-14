---
title: 简单动态字符串SDS
date: '2022-04-14 14:43'
swiper: false
categories: 《Redis设计与实现》读书笔记
tags:
  - Redis
swiperImg: 'https://jktql.oss-cn-shanghai.aliyuncs.com/wallpaper/9.png'
img: 'https://jktql.oss-cn-shanghai.aliyuncs.com/wallpaper/9.png'
top: false
abbrlink: 2337298088
---


# 简单动态字符串SDS

*   Redis中，涉及可以被修改的字符串值时，都用**简单动态字符串**（simple dynamic string，SDS）来实现

*   SDS还被用作缓冲区，比如AOF模块中的AOF缓冲区，客户端状态中的输入缓冲区

### SDS的定义

```java
struct sdshdr{
    //buf已使用的字节数
    int len;
    //buf未使用的字节数
    int free;
    //字节数组，用于保存字符串
    char buf[];
}
```

![](https://jktql.oss-cn-shanghai.aliyuncs.com/article/简单动态字符串SDS/image_f1A7pv8nZyKsKzs7qGRMiJ.png)

如上图所示，5字节未使用空间，已使用5字节，buf\[]存储了字符串值，最后一个字节保存了空字符`'\0'`。这里要注意的是，free和len的计算不涉及空字符`'\0'`

### SDS和c字符串的区别

**为什么redis要使用SDS不用c字符串呢？**

*   简单的说就是c字符串不满足redis对字符串在**安全性**、**效率**和**功能**上的要求

*   具体来说：

    *   c字符串不记录长度，所以获取字符串长度效率较差、拼接字符串容易导致缓冲区溢出、每次拼接或缩短字符串时都需要内存重分配

    *   c字符串不能保存二进制数据，因为c字符串用`'\0'`来判断字符串结束。如果要保存多个单词，用`'\0'`隔开，c字符串就会自动忽略后面的单词

#### SDS如何解决这个问题的呢？

*   可以调用len直接获取长度

*   不会造成缓冲区溢出，当拼接时会先判断空间是否满足，不满足会扩容

*   SDS采用**空间预分配**和**惰性空间释放**两种策略，拼接前判断空间不足会预分配，缩短时并不立即回收空间，在有需要时真正释放空间

*   SDS判断字符串结束用的是len而不是`'\0'`来判断字符串结束，所以可以保存二进制数据

*   SDS虽然用len判断字符串结束，但依然用`'\0'`来结尾，所以可以使用一部分\<string.h>的函数

![](https://jktql.oss-cn-shanghai.aliyuncs.com/article/简单动态字符串SDS/image_gMouDbiuQY3GjxnTW8Jb3f.png)

![](https://jktql.oss-cn-shanghai.aliyuncs.com/article/简单动态字符串SDS/image_8MrRXUasjE8WtkuVTEEPx4.png)
