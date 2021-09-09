---
title: 共享变量与Cache
date: '2021-09-09 21:29'
swiper: false
categories: 《Apache Spark设计与实现》读书笔记
tags:
  - Spark
swiperImg: >-
  https://img13.360buyimg.com/ddimg/jfs/t1/199860/32/7610/2589623/613a0c74Ec860efbf/f4d400e42f7dc504.png
img: >-
  https://img13.360buyimg.com/ddimg/jfs/t1/199860/32/7610/2589623/613a0c74Ec860efbf/f4d400e42f7dc504.png
top: false
abbrlink: 4244340064
---



**默认情況下，一个算子函数中使用到了某个外部的变量，那么这个变量的值会被拷贝到每个task中，此时每个task只能操作自己的那份变量数据**
**Spark提供了两种共享变量，一种是 Broadcast Variable(广播变量)，另一种是 Accumulator(累加变量)**

---

## Broadcast Variable（广播变量）
> **Broadcast Variable（广播变量）会把指定的变量拷贝一份到每个节点上**
> - **通过调用 SparkContext.broadcast(指定变量) 方法为指定的变量创建 只读 的广播变量，通过 广播变量.value() 方法获取值**
> - **优点：**
>    - **如下图所示，如果不使用广播变量，当map计算时会把外部变量拷贝到每个task中，当一个节点task很多的时候会消耗很多资源。用广播变量的话，每个节点只拷贝一份，大大提高了性能**
>
![](/medias/共享变量与Cache/0.png)


---

## Accumulator（累加器）
**Accumulator 只能 专用于累加，并且除了Drive进程以外，其他进程都不能读取值**
**直接看案例就懂了**
```scala
val sc = SparkSession.builder().getOrCreate().sparkContext

//直接用外部变量获取RDD中元素的和
	var sum = 0
	sc.parallelize(Array(1,2,3)).foreach( sum += _)
	println(sum)
打印结果: 0
原因是外部变量是在Drive进程中的，用foreach算子计算的和是局部变量传不到Drive，在Drive中println是打印不出来的

//用Accumulator获取RDD中元素的和
	var sum = sc.longAccumulator
	sc.parallelize(Array(1,2,3,4)).foreach(sum.add(_))
	println(sum.value)
打印结果：10
在Drive进程中可以调用Accumulator变量.value得到累加结果
```

---

## Cache
![](/medias/共享变量与Cache/1.png)

- **在未引入Cache时：**
   - **如图所示，因transformation算子有lazy特性，在action之前不会执行。所以当计算result1时，会走一遍step1->2->3，当计算result2时，还会走一遍step1->2->3，极大浪费资源。**
- **那么现在引入Cache：**
   - **在RDD2添加Cache后，计算result2时可以直接从Cache中取出计算过的RDD2即可，无需重复计算RDD2**

**由此可见，在需要重复调用的RDD上非常有必要添加Cache，直接使用`RDDname.cache()`即可**
