---
title: 第3章 MySQL日志
date: '2021-08-06 21:25'
swiper: false
categories: 《MySQL技术内幕》读书笔记
tags:
  - MySQL
swiperImg: https://img11.360buyimg.com/ddimg/jfs/t1/182087/34/18220/2525891/610d3a33Eb4b7dbeb/816ad5bde8c6daba.png
img: https://img11.360buyimg.com/ddimg/jfs/t1/182087/34/18220/2525891/610d3a33Eb4b7dbeb/816ad5bde8c6daba.png
top: false
abbrlink: 4156801793
---
## MySQL常用的日志类型有哪些？
![](/medias/第3章MySQL日志/0.png)

## 错误日志
**错误日志记录mysql在启动、运行、关闭过程中出现的问题，并会记录在错误文件中。用户可以通过`SHOW VARIABLES LLKE 'log_error‘`来定位错误日志文件。默认情况下文件名为主机名，查看错误文件并进行优化**

## 慢查询日志
**慢查询日志可以定位可能存在问题的SQL语句，从而进行SQL语句层面的优化**
**例如可以在MySQL启动时设一个阈值，若运行时间超过该值的SQL语句就记录到慢查日志文件中**
**用户可以通过`SHOW VARIABLES LIKE 'log_slow_queries'`**

## 二进制日志
**二进制日志记录了对MySQL数据库执行更改的所有操作，即不包括SHOW和SELECT这类语句**
**二进制日志的作用为基于时间点恢复数据、主从复制数据、审计数据（判断是否有注入攻击）**
**默认文件名为主机名.日志序列号，如host.00001。二进制日志默认关闭，需要手动开启**
