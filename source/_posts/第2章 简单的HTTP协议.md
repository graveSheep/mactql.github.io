---
title: 第2章 简单的HTTP协议
date: '2021-07-02 10:27'
swiper: false
categories: 《图解HTTP》读书笔记
tags:
  - 计算机网络
swiperImg: >-
  https://img10.360buyimg.com/ddimg/jfs/t1/146833/35/3948/643829/5f1f6f0bEd22b508a/8df9517da71339dd.jpg
img: >-
  https://img10.360buyimg.com/ddimg/jfs/t1/146833/35/3948/643829/5f1f6f0bEd22b508a/8df9517da71339dd.jpg
top: false
abbrlink: 53019385
---

---

## 2.2 HTTP请求和响应报文格式
![](https://img10.360buyimg.com/ddimg/jfs/t1/180478/2/12183/160617/60de6ccaE6ddb17a3/758649c3c46df958.jpg)

---

## 2.5 常用HTTP方法有哪些？
> - **GET：请求访问服务器某个资源**
> - **POST：和GET对应，传输某个资源**
> - **PUT：传输某个文件**
> - **HEAD：与GET相同，但只想获得报文首部，不返回数据，例如想要查询某个资源是否存在，不需要获取数据**
> - **DELETE：删除服务器某个资源**
> - **OPTIONS：查询URI某个资源支持的方法，例如返回GET、POST**


---

## 2.8 Cookie
### 为什么要cookie？
要求登陆认证的web页面无法保存登陆状态，每次跳转页面都要再次登陆，为了避免这种频繁登陆，需要cookie保存登陆状态
### 怎么使用cookie？

- **第一次登陆后，服务器返回响应，响应报文中添加一个cookie通知客户端保存cookie**
- **以后每次请求，在报文中都添加一个cookie值，服务器检查cookie值的记录，有的话就不需要登陆了**

![](https://img12.360buyimg.com/ddimg/jfs/t1/190040/20/11105/187775/60de788dE6941cef1/6043b1e603cef490.jpg)
