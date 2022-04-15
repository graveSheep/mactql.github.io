---
title: Redis字典
date: '2022-04-15 19:40'
swiper: false
categories: 《Redis设计与实现》读书笔记
tags:
  - Redis
swiperImg: 'https://jktql.oss-cn-shanghai.aliyuncs.com/wallpaper/0.png'
img: 'https://jktql.oss-cn-shanghai.aliyuncs.com/wallpaper/0.png'
top: false
abbrlink: 2919167555
---


# Redis字典

字典是用于保存键值对的抽象数据结构。当一个哈希键包含的键值对比较多时，或者键值对中的元素都是比较长的字符串时，Redis就会使用字典作为哈希键的底层实现

### 字典的定义

Redis的字典使用**哈希表**作为底层实现，一个哈希表里面可以有**多个哈希表节点**，每个哈希表节点保存了字典中的**一个键值对**

哈希表的定义如下：

```c
typedef struct dictht{
    //哈希表数组
    dictEntry **table;
    //哈希表大小
    unsigned long size;
    //哈希表大小掩码，用于计算索引值
    //总是等于size-1
    unsigned long sizemask;
    //该哈希表已有节点的数量
    unsigned long used;
}dictht;
```

哈希表的每一个元素都是一个哈希表节点，节点的实现如下：

```c
typedef struct dictEntry{
    //键
    void *key;
    //值
    union{
        void *val;
        uint64_t u64;
        int64_t s64;
    } v;
    //指向下个哈希表节点，形成链表
    struct dictEntry *next;
} dictEntry;
```

#### 哈希算法

Redis计算哈希值方法： `hash=dict->type->hashFunction(key);`

计算索引值的方法：`index=hash & dict->ht[x].sizemask;`

举个例子，假设要插入的键值对是\<k,v>，然后公式计算哈希值，假设得到hash=8，然后计算索引值`index= 8 & 3 = 0`，如下图所示插入即可

![](https://jktql.oss-cn-shanghai.aliyuncs.com/article/Redis字典/image_46cNiFeBTwbSibcfCodmmc.png)



#### 通过链地址法解决键冲突

![](https://jktql.oss-cn-shanghai.aliyuncs.com/article/Redis字典/image_oYucXg8uPiWDSp61hSw6JD.png)

### Redis扩容和缩容

当Redis中键值对太多或太少，则需要扩容和缩容，即rehash

rehash步骤如下：

1.  为字典ht\[1]哈希表**分配空间**，大小取决于要执行的操作与ht\[0]**当前键值对的数量**

2.  将保存在ht\[0]中的所有键值对存放到ht\[1]指定的位置

3.  当ht\[0]的所有键值对都迁移完毕后，**释放ht\[0]**，并**指向**ht\[1]，并在ht\[1]上创建一个空的哈希表，为下次rehash准备

需要注意的是，这个rehash是渐进式的，因为如果ht\[0]的键值对很多的话，向ht\[1]迁移会导致服务器在一段时间内停止服务，为了避免这种情况会慢慢的rehash到ht\[1]中。具体操作是，同时维护ht\[0]和ht\[1]两张哈希表，任何操作都会在两张表上进行，例如查找键时先去ht\[0]找，找不到去ht\[1]找。添加操作直接去ht\[1]添加

![](https://jktql.oss-cn-shanghai.aliyuncs.com/article/Redis字典/image_hZxa7DtuA6yXKv8snYA7Kt.png)
