---
title: Scala函数式编程
date: '2021-09-02 15:26'
swiper: false
categories: 《7天极速掌握Scala》课程笔记
tags:
  - Scala
swiperImg: >-
  https://img11.360buyimg.com/ddimg/jfs/t1/205097/13/4233/1197609/61307ceaEb04292c7/2437446d6b2ee2e1.png
img: >-
  https://img11.360buyimg.com/ddimg/jfs/t1/205097/13/4233/1197609/61307ceaEb04292c7/2437446d6b2ee2e1.png
top: false
abbrlink: 496349428
---



## Scala函数式编程特性一：函数赋值给变量
- **把函数赋值给变量,函数名+空格+_**
```scala
//首先有一个函数
def fun(A:String){
	...
}
//把函数赋值给变量,空格+_即可
val A = fun _
//以后就可以直接用变量名代替函数名
A("abc")
```

---

## Scala函数式编程特性二：匿名函数

- **匿名函数：(参数名:参数类型)=>函数体**
```scala
val funname = (A:String)=> println(A)
```

---

## Scala函数式编程特性三：高阶函数

- **高阶函数：把函数作为参数传给另一个函数**
- **定义高阶函数时，高阶函数的参数列表中：**
   - **要写清楚传入函数的参数，当前函数名:(源函数参数)=>源函数返回值类型**
   - **还要写源函数参数，源函数参数：源函数参数类型**
```scala
val funA = (A:String)=> println(A) //定义匿名函数
def funB(fun:(String)=>Unit,name:String){
  fun(name) //在高阶函数中调用函数
} //定义高阶函数

//两种方法调用高阶函数
funB(funA,"hello"）//第一种：直接传函数名调用高阶函数
funB((A:String)=> println(A),"hello") //第二种：直接传整个匿名函数调用高阶函数

对于匿名函数调用的方法还可以简写：
funB((A)=>println(A),"hello")
当只有一个参数时还可以 funB(A=>println(A),"hello")
```

---

## 常用的一些高阶函数的使用

- **Map：对集合中每个元素都应用一个函数，返回应用后的元素列表**
```scala
//例如把数组全部元素*2
Array(1,2,3,4,5).map(num=>num*2) 在map高阶函数中传入匿名函数
//也可以简写成
Array(1,2,3,4,5).map(_ * 2)
```

- **flatMap：首先对每个元素执行Map，但是会把每个元素执行的结果再合并成一个大集合并返回**
```scala
//例如把字符串数组中的字符串按照空格切开
Array("hello you","hello me").flatMap(line=>line.split(" "))
//也可以简写成
Array("hello you","hello me").flatMap(_.split(" "))
```

- **foreach：迭代的意思**
```scala
//例如输出数组每个元素
Array(1,2,3).foreach(A=>println(A))
//也可以简写成
Array(1,2,3).foreach(println(_))
```

- **filter：按照函数进行过滤操作**
```scala
//例如过滤出数组中的偶数
Array(1,2,3,4,5).filter(A => A % 2 == 0)
//也可以简写成
Array(1,2,3,4,5).filter(_ % 2 == 0)
```

- **reduceLeft：按照函数从左往右的两两元素进行操作，例如累加、求最大值等**
```scala
//求数组的和
Array(1,2,3).reduceLeft((A,B)=>A+B)
//也可以简写成
Array(1,2,3,4,5).reduceLeft(_+_)
```
