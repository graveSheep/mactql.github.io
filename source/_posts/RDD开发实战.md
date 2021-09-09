---
title: RDD开发实战
date: '2021-09-09 09:43'
swiper: false
categories: 《Apache Spark设计与实现》读书笔记
tags:
  - Spark
swiperImg: >-
  https://img12.360buyimg.com/ddimg/jfs/t1/73365/34/17530/1566536/61396711Ec6fc2d09/d36d32e559da9111.png
img: >-
  https://img12.360buyimg.com/ddimg/jfs/t1/73365/34/17530/1566536/61396711Ec6fc2d09/d36d32e559da9111.png
top: false
abbrlink: 1890251266
---


## 如何创建RDD？
- **创建RDD有三种方式**
   - **基于集合创建RDD：使用sparkContext的parallelize()方法，第一个参数传入集合，第二个参数传入partition数量。Spark会为每个partition执行一个task**
```scala
val spark = SparkSession.builder().getOrCreate()
val arr = Array(1,2,3,4)
val rdd = spark.sparkContext.parallelize(arr,4) //基于Array创建一个4分区的rdd
```

   - **基于本地或HDFS文件创建RDD：使用sparkContext的textFile()方法，第一个参数传入文件路径，第二个参数传入partition数量**
```scala
val spark = SparkSession.builder().appName("WordCount").getOrCreate()
val text = spark.sparkContext.textFile("/path/words.txt",3)
```

---

## Spark中对RDD的操作有哪些？

- **在Spark中，对RDD的操作只有两种，Transformation 和 Action**
- **Transformation**
   - **是对已有的RDD转化为新的RDD，如flatMap、Map等操作**
   - **lazy特性，在没有执行Action之前，所有的操作都只是得到一个逻辑上的RDD，内存中没有任何数据**



- **Action**
   - **是对RDD最后的操作，如foreach，reduce，返回结果给Driver进程等操作**
   - **只有当执行到Action代码，才会触发之前所有的Transformation算子的执行**

---

## Transformation算子实战
![](/medias/RDD开发实战/0.png)
```scala
val sc = SparkSession.builder().getOrCreate().sparkContext

//map算子：集合每个元素乘2
sc.parallelize(Array(1,2,3,4,5)).map(_ * 2)

//filter算子：过滤集合中的偶数
sc.parallelize(Array(1,2,3,4,5)).filter(_ % 2 == 0)

//flatMap算子：把每行字符串拆分成单词
sc.parallelize(Array("ns tql","jk tcl")).flatMap(_.split(" "))

//groupByKey算子：对<<出生地,姓名>>集合根据出生地分组
sc.parallelize(Array(("wuxi","ns"),("shandong","jk1"),("wuxi","jk2"))).groupByKey()

//reduceByKey算子：对<<word,1>>集合计算每个word出现的次数
sc.parallelize(Array(("ns",1),("jk",1),("ns",1))).reduceByKey(_+_)

//sortByKey算子：对<<收入,姓名>>集合根据收入降序排序
sc.parallelize(Array((10000,"ns"),(100,"jk"))).sortByKey(false)

//join算子：对<<姓名，收入>>和<<姓名，出生地>>两个集合基于姓名进行合并
sc.parallelize(Array("ns",10000),("jk",100)).join(sc.parallelize(Array(("ns","wuxi"))))
合并结果是：Array(("ns",(10000,"wuxi")),("jk",100))

//distinct算子：去除集合中重复元素
sc.parallelize(Array(1,3,1,2,3))

```

---

## Action算子实战
![](/medias/RDD开发实战/1.png)
```scala
val sc = SparkSession.builder().getOrCreate().sparkContext

//reduce算子：求数组元素的和
sc.parallelize(Array(1,2,3)).reduce(_+_)

//collect算子：返回RDD中的元素集合
val res = sc.parallelize(Array(1,2,3)).collect()
返回的是：Array(1,2,3)

//take(n)算子：获取RDD中前2个元素
val res = sc.parallelize(Array(1,2,3)).take(2)
返回的是：Array(1,2)

//count算子：获取RDD元素个数
val res = sc.parallelize(Array(1,2,3)).count()
返回的是：3

//saveAsTextFile算子：保存RDD中元素到HDFS上去
sc.parallelize(Array(1,2,3)).saveAsTextFile("hdfs://hdfs路径")

//countByKey算子：对计算元祖的每个Key出现的次数
sc.parallelize(Array(("ns",100),("ns",12),("jk",14))).countByKey()
返回的是：("ns",2),("jk",1)

//foreach算子：遍历输出RDD元素
sc.parallelize(Array(1,2,3)).foreach(println(_))

```
