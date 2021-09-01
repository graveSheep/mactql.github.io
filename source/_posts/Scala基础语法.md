---
title: Scala基础语法
date: '2021-09-01 9:32'
swiper: false
categories: 《7天极速掌握Scala》读书笔记
tags:
  - Scala
swiperImg: https://img12.360buyimg.com/ddimg/jfs/t1/203993/13/4185/3662146/612ed9f4Eb48bff14/dce4c387502b092b.png
img: https://img12.360buyimg.com/ddimg/jfs/t1/203993/13/4185/3662146/612ed9f4Eb48bff14/dce4c387502b092b.png
top: false
abbrlink: 2823487899
---



## 如何申明变量和常量
- **val：常量**
- **var：变量**
```scala
//数据类型如果不指定，会自动根据表达式来推断
val answer = 0
//也可以指定数据类型
val answer: Int = 1
```
### 那么Scala有哪些数据类型呢？

- **基本数据类型：Byte,Char,Short,Int,Long,Float,Double,Boolean**
- **增强版数据类型：StringOps、RichInt、RichChar、RichDouble等（比基本类型多了上百种功能）**
   - **就以RichInt为例：`1.to(10)` 相当于Range 1 to 10**

---

## Scala的 if 和Java是不同的
**区别在于Scala的if是有返回值的，Java的if是没有的**
**举个例子：`val ret = if(18>1) 1 else 0` 这里 ret 会接收 if 的返回值 1**

---

## Scala的for和Java也不同，while相同
**`for(i <- 1 to/until n)` 意思就是 i 从1到n/n-1迭代**
**甚至可以迭代字符串中每个字符`for(c <- "string") println(c)`**
**还有高级for循环：**

- **if守卫：`for(i <- 1 to 10 if i % 2 == 0) println(i)` 就是把if判断写在for里面不满足就continue**
- **yield：`for(i <- 1 to 3) yield i * 2` 可以得到Vector(2，4，6) 就是在for循环中得到的数据组合成一个集合**

---

## Scala中的数组和Java类似

- **`val array = new Array[type](数组长度)`**
- **也可以这样写 `val array = Array("....",23,"..")`**
- **甚至还有像ArrayList那样的可变长度的数组 `val ab = new ArrayBuffer[Int]()`**
- **还有一个元祖tuple也很常用，可存不同类型的数据 `val t = (..,...,...);` 并且可以用`t._i`来获取指定数据**

---

## Scala中也有集合Set、List、Map

- **`val s = Set(1,2,3)`这样就直接创建了一个不可变的Set集合，还有HashSet、LinkedHashSet、SortedSet**
- **`val l = List(1,2,3)` 这样就直接创建了一个不可变的List集合**
   - **List有很多方法，如`l.head`，`l.tail`，`for(i <- l) println(i)`**
   - **ListBuffer是一个可变型的List集合`val lb = scala.collection.mutable.ListBuffer[Int]()`**
- **`val m = Map(("A",1),("B",2))` 这样就直接创建了一个不可变的Map集合**
- **需要注意的是：**
   - **如果创建的是一个可变型的集合，添加删除元素可以直接用 +=、-=**
   - **默认用Set、List、Map创建的都是不可变的集合，可以用`Scala.collection.mutable.Set/ListBuffer/Map[type](参数列表)`**

---

## Scala的函数和Java的方法也不一样
```scala
//需要返回值的函数
def fun(A:type,B:type) = {
  ...
  ...
  A,B 最后一行就是返回值，不需要return
}

//还有不需要返回值的函数
def fun(A:type,B:type) { //没有=号就是没有返回值
  ...
  ...
}
```
