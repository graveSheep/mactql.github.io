---
title: Scala高级特性
date: '2021-09-02 16:26'
swiper: false
categories: 《7天极速掌握Scala》课程笔记
tags:
  - Scala
swiperImg: >-
  https://img12.360buyimg.com/ddimg/jfs/t1/187053/13/21388/2033103/61308749E5ab1e4d1/837800fd877e1d8b.png
img: >-
  https://img12.360buyimg.com/ddimg/jfs/t1/187053/13/21388/2033103/61308749E5ab1e4d1/837800fd877e1d8b.png
top: false
abbrlink: 159453455
---



## Scala高级特性一：模式匹配
- **Scala模式匹配类似于Java的switchcase，但是更加强大，甚至可以匹配变量类型、集合元素、有值没值**
- **语法格式为：变量 match { case值 => 代码 }**
```scala
首先如何匹配变量类型
def whichtype(A: type){ //匹配变量类型是否是type1、type2、type3
	A match{
  	case a:type1 => ...
    case b:type2 => ...
    case _:type  => ...

  }
}

如何匹配有值没值
def isNull(A :type){
	A match{
  	case None : ...
    case _ : ....
  }
}
```

---

## Scala高级特性二：隐式转换

- **Scala可以在class或者object中定义隐式转换函数，定义后的对应的实例在需要时会自动转换成另一个类型的实例**
```scala
//例如让狗抓老鼠
class cat(val name:String){
	def catmouse(){...} //抓老鼠是cat类的函数
}
Object dog(val name:String){
	implicit def dogtocat(d : dog) = new Cat()
  new dog().catmouse() //因为设置了dogtocat隐式转换函数，所以会自动转换成cat并调用抓老鼠方法
}
```
