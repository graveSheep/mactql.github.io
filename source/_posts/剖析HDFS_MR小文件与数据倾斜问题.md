---
title: 剖析HDFS/MR小文件与数据倾斜问题
date: '2021-09-24 12:56'
swiper: false
categories: 《拿来就用的企业级解决方案》课程笔记
tags:
  - HDFS
  - MapReduce
swiperImg: >-
  https://img14.360buyimg.com/ddimg/jfs/t1/112803/13/20222/1721407/614d5acaE5a67f717/0a4edf576b50c2a7.png
img: >-
  https://img14.360buyimg.com/ddimg/jfs/t1/112803/13/20222/1721407/614d5acaE5a67f717/0a4edf576b50c2a7.png
top: false
abbrlink: 2599323417
---



## 什么是小文件问题？
- **HDFS上如果小文件很多，每个小文件都会在NameNode中占用150字节的内存空间**
- **而在MR中每个小文件都会占一个block，每个block都会产生数据分片对应一个Map任务，导致Map任务特别多，消耗了很多启动Map任务的性能**



## 如何解决小文件问题？
**HDFS提供了两种容器，SequenceFile 和 MapFile**

- **SequenceFile**
   - **是一种二进制文件，会直接把<key,Value>的形式序列化到文件中**
   - **所以，我们可以把小文件进行合并成键值对，Key为文件名，文件内容作为Value，这样序列化组成一个大文件**
   - **缺点：合并后不容易查看，需要通过遍历才能看每个小文件**
- **MapFile**
   - **是排序后的SequenceFile**
   - **MapFile有两部分，分别是index和data。其中index记录key，以及data在文件中的偏移量。**
   - **优点：查询文件时，可以通过index快速找到数据位置**

---

## 什么叫数据倾斜问题？

- **比如文件里有1000w条数据，里面都是1和0，但是1的数据有900w条，0的数据只有100w条，所以1就是数据倾斜了，这样造成的结果就是处理1的Reduce任务很慢很慢，处理0的Reduce任务早就好了**
- **总结：MR任务执行时，大部分Reduce节点都处理完毕，但有一个或几个Reduce任务很慢很慢，导致整个Reduce任务很慢**



## 怎么解决数据倾斜问题？
**有两种解决方案：**

- **增加Reduce任务个数：治标不治本**
- **把倾斜的数据打散：比如1倾斜，可以把1改成1_0、1_1等，分到多个Reduce中即可**
