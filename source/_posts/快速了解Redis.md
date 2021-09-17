---
title: 快速了解Redis
date: '2021-09-17 10:00'
swiper: false
categories: 《快速上手内存数据库Redis》课程笔记
tags:
  - Redis
swiperImg: >-
  https://img13.360buyimg.com/ddimg/jfs/t1/6006/9/13426/1214059/6143f72eEc8701381/148f03291c2e051b.png
img: >-
  https://img13.360buyimg.com/ddimg/jfs/t1/6006/9/13426/1214059/6143f72eEc8701381/148f03291c2e051b.png
top: false
abbrlink: 4199058362
---



## 什么是Redis？
- **Redis是一个高性能的基于内存的Key-Value数据库**
- **可以在N多条记录中根据条件非常快的查找一条或几条记录**

---

## Redis的数据格式是什么样的？

- **Redis数据格式为Key-Value**
   - **Key：String**
   - **Value：String、Hash、List、Set、SortedSet......**

---

## Redis应用场景有哪些？

- **最常用来当作缓存系统：当用户需要向数据库取数据时，先看redis有没有，没有就去数据库里拿到redis中再从redis中取数据**
- **计数器：新浪微博的评论数、点赞数**
- **消息队列：不过用Kafka比较多了**

---

## Redis基础命令有哪些？
![](/medias/快速了解Redis/0.png)
```scala
//添加一个键值对
set【key】【value】 //例如set a 1

//获取指定key的value
Keys【key】//例如Keys a

//删除指定键值对
del【key】//例如del a
```

---

## Redis多数据库特性
**Redis有16个数据库【0-15】，默认在0号数据库，可以用select n 来指定数据库**
