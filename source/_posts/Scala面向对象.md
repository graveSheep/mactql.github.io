---
title: Scala面向对象
date: '2021-09-01 15:32'
swiper: false
categories: 《7天极速掌握Scala》课程笔记
tags:
  - Scala
swiperImg: >-
  https://img13.360buyimg.com/ddimg/jfs/t1/189574/33/21207/2168096/612f2a71E86397f28/f6dccf7ee2064802.png
img: >-
  https://img13.360buyimg.com/ddimg/jfs/t1/189574/33/21207/2168096/612f2a71E86397f28/f6dccf7ee2064802.png
top: false
abbrlink: 496349427
---




## Scala的类和对象几乎和Java一样
```scala
class Point(xc: Int, yc: Int) { //构造函数是直接放在Class的参数列表里，这里和Java不同
   var x: Int = xc
   var y: Int = yc

   def move(dx: Int, dy: Int) {
      x = x + dx
      y = y + dy
      println ("x 的坐标点: " + x);
      println ("y 的坐标点: " + y);
   }
}
```

- **还有一种不需要类就可以创建对象的方法，直接用Object关键字，相当于Java的静态类**
```scala
object Person{
	var age
  ...
  ...
}
使用时不需要new，可以直接对象名.成员,如下
println(Person.age)
```

- **需要注意的是：**
   - **如果object和class同名，他们为伴生关系，可以互相访问私有属性**
   - **可以在伴生object中创建一个apply函数，可以调用这个函数直接得到伴生class的对象实例**

---

## Scala也必须要一个main方法才能运行
```scala
object mainTest {//main方法只能定义在object中，不能在class中
   def main(args: Array[String]) {
   }
}
```

---

## Scala中的接口trait也比较特殊
```scala
trait TraitA {
  def A(x: Int)
}
trait TraitB {
  def A(x: Int)
}

class Person extends TraitA with TraitB{//实现用extends，多实现后面用with连接
	override TraitA(x:Int){
  	...
  }
  TraitB(x:Int){//可以写override，也可以不写
  	...
  }
}
```
