---
title: 第18章 java I/O
date: '2021-06-30 10:01'
swiper: true
categories: 《Java编程思想》读书笔记
tags:
  - Java基础
swiperImg: >-
  https://img10.360buyimg.com/ddimg/jfs/t1/186273/40/11828/351410/60dbd17aE0c517910/dd9fee68898c4f4c.jpg
img: >-
  https://img10.360buyimg.com/ddimg/jfs/t1/186273/40/11828/351410/60dbd17aE0c517910/dd9fee68898c4f4c.jpg
top: false
abbrlink: 3136801953
---

## java的IO分为字符流和字节流：

- **字节流一般处理图像数据或字节文件这类的二进制数据，其他数据一般是字符流**

> **字符流：（以输入流为例）**
> - **字符流中最基本的CharArrayReader和StringReader，从字符数组或字符串的数据元中读取字符**
> - **还有三个复杂功能的类：**
>    - **BufferedReader，对原始数据频繁的读会比较慢，可以采用用缓冲区读写，效率更高**
>    - **FilterReader抽象类，创建时需要传入一个Reader对象叠加新的功能，可以跳跃字符流中特定字符等操作**
>    - **InputStreamReader，把字节流转化为字符流。常用FileReader子类，从字节文件中转化为字符流读取**


> **字节流：（以输入流为例）**
> - **字符流中最基本的ByteArrayInputStream和FileInputStream，从字节数组或字节文件的数据元中读取字节**
> - **还有复杂功能的类：**
>    - **FilterInputStream抽象类，常用继承它的子类如下：**
>       - **BufferedInputStream，对原始数据读写频繁会很慢，采用从缓冲区不停的读写，效率更高**
>       - **DataInputStream和DataOutputStream可以从字节流中读写数据并转换成基本数据类型**

## 导图如下：
![](https://img11.360buyimg.com/ddimg/jfs/t1/184379/15/11818/205478/60dbcff6E9fde4ddb/8a843a85dd6094a9.jpg)
