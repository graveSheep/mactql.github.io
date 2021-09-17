---
title: 初识Spark与工作原理
date: '2021-09-06 14:59'
swiper: false
categories: 《Spark快速上手》课程笔记
tags:
  - Spark
swiperImg: >-
  https://img10.360buyimg.com/ddimg/jfs/t1/204490/27/5830/1455812/613a0fbbE393f2cd6/d6eca297f4f4972b.png
img: >-
  https://img10.360buyimg.com/ddimg/jfs/t1/204490/27/5830/1455812/613a0fbbE393f2cd6/d6eca297f4f4972b.png
top: false
abbrlink: 2693573150
---


## 需求分析：
**读取文件所有内容，统计每个单词出现的次数**

---

## 首先介绍一下如何用Scala在本地运行WordCount

1. **第一步，首先要构建Application的运行环境，Driver创建一个SparkContext**
```scala
val conf = new SparkConf()
conf.setAppName("WordCount") //设置作业名称
	.setMaster("local") //设置在本地运行
val sc = new SparkContext(conf)  //通过Conf参数创建一个SparkContext
```

2. **第二步，加载数据并转化成RDD**
```scala
val lineRDD = sc.textFile("HDFS路径或者磁盘文件的路径")
```

3. **第三步，对数据进行切割，把一行数据切成一个个单词**
```scala
val wordsRDD = lineRDD.flatMap(_.split(" ")) //flatMap使用高阶函数，这里对空格进行分割，处理后形成新的RDD
```

4. **第四步，迭代words，把每个word转化成(word，1)的键值对形式**
```scala
val pairRDD = wordsRDD.map((_,1))
```

5. **第五步，根据Key进行分组聚合统计**
```scala
val wordCountRDD = pairRDD.reduceByKey(_ + _)
```

6. **第六步，打印结果并关闭SparkContext**
```scala
wordCountRDD.foreach(wordCount=>println(wordCount._1+"--"+wordCount._2))
sc.stop()
```
