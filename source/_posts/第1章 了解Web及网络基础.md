---
title: 第1章 了解Web及网络基础
date: '2021-07-01 20:38'
swiper: false
categories: 《图解HTTP》读书笔记
tags:
  - 计算机网络
swiperImg: >-
  https://img12.360buyimg.com/ddimg/jfs/t1/184864/26/12124/268673/60ddb9b1E0c5b639a/56bc83e09b987289.jpg
img: >-
  https://img12.360buyimg.com/ddimg/jfs/t1/184864/26/12124/268673/60ddb9b1E0c5b639a/56bc83e09b987289.jpg
top: false
abbrlink: 3376318152
---
## 1.3.3 TCP/IP通信是怎么传输的？
![](https://img12.360buyimg.com/ddimg/jfs/t1/175791/30/17454/177642/60dd6f1fE8814f6d1/ad21adf93aa8afe2.jpg)
> - **从下到上以此是链路层、网络层、传输层、应用层**
>    - **第一个是链路层，解析的是以太网首部，包含源MAC地址和目标MAC地址**
>       - **在一个网络之内，也就是一"跳"之内进行MAC转发，具体看 [怎么根据MAC地址转发](https://mactql.github.io/posts/165302757.html#3-2-4-%E6%80%8E%E4%B9%88%E6%A0%B9%E6%8D%AEMAC%E5%9C%B0%E5%9D%80%E8%BD%AC%E5%8F%91%EF%BC%9F)**
>    - **第二个是网络层，解析的是IP首部，包含源IP地址和目标IP地址**
>       - **首先通过ARP查找下一"跳"对应的MAC地址，然后通过链路层实现在每一"跳"之间通信，最终和目标通信，具体看 [ARP是什么](https://mactql.github.io/posts/837272352.html#5-3-ARP)**
>    - **第三个是传输层，解析的是TCP首部，包含源进程端口号和目标进程端口号**
>       - **将大块数据分成多个报文段，并发起TCP三次握手，具体看 [说一下三次握手](https://mactql.github.io/posts/3865951273.html#%E8%AF%B4%E4%B8%80%E4%B8%8B%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B%EF%BC%9F%EF%BC%88%E5%BB%BA%E7%AB%8B%E8%BF%9E%E6%8E%A5%EF%BC%89)**
>    - **最后是应用层，DNS解析以及发送HTTP请求**


---

## 1.7 URI和URL
> - **首先URL是URI的子集**
> - **唯一标识网络中的资源就是URI，如果他是一条路径就是URL**
