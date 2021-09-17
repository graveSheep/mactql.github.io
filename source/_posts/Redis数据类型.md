---
title: Redis数据类型
date: '2021-09-17 10:48'
swiper: false
categories: 《快速上手内存数据库Redis》课程笔记
tags:
  - Redis
swiperImg: >-
  https://img12.360buyimg.com/ddimg/jfs/t1/198978/13/8800/843494/61440246E77f7a394/d2cf08cdd440bc1c.png
img: >-
  https://img12.360buyimg.com/ddimg/jfs/t1/198978/13/8800/843494/61440246E77f7a394/d2cf08cdd440bc1c.png
top: false
abbrlink: 950473165
---



## Redis常见数据类型
**上一章我们了解了Redis常见的五种数据类型，string、set、hash、sortedset、list，这里我们详细介绍一下**

---

### 首先是string
**string可以存任何形式的内容，甚至是二进制数据或图片**
![](/medias/Redis核心实践/0.png)
**在这些操作的基础上还有一次添加多个：mset 和一次查多个： mget**

---

### hash类型
**hash类型存的是字段和字段值的映射，类似是在存键值对，只能是字符串，常用来存对象**
![](/medias/Redis核心实践/1.png)
**这里的有三个属性，key、field、name，其中field和name是key的value，而field是字段value是字段值，相当于是把一个键值对存在redis中，key是这个键值对的key**

---

## list类型
**list是一个有序的字符串列表，而且是双向链表，常用来当作队列使用**
![](/medias/Redis核心实践/2.png)

---

## set类型
**set集合中的元素都是不重复且无序的**
![](/medias/Redis核心实践/3.png)

---

## sortedset类型
**与set不同的是有序集合，相当于为每个元素指定一个分数，常用于获取topN的场景**
![](/medias/Redis核心实践/4.png)
**注意用zadd添加元素要`zadd key score value` 这样写，一定要在value前给他一个分数**
