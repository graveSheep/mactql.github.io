---
title: 第1章 MySQL和存储引擎
date: '2021-08-06 09:32'
swiper: false
categories: 《MySQL技术内幕》读书笔记
tags:
  - MySQL
swiperImg: https://img13.360buyimg.com/ddimg/jfs/t1/195921/10/16895/978846/610c9223Ed104f45e/ac525b4a000e7b64.png
img: https://img13.360buyimg.com/ddimg/jfs/t1/195921/10/16895/978846/610c9223Ed104f45e/ac525b4a000e7b64.png
top: false
abbrlink: 925095689
---


## MySQL存储引擎是什么？
- **MySQL中的数据、索引以及其他对象是如何存储的，是一套文件系统的实现**

---

## MySQL存储引擎的选择

- **5.5之前默认存储引擎是MyISAM,5.5之后默认存储引擎是Innodb**

---

## Innodb和MyISAM的区别

- **Innodb支持事务，MyISAM不支持事务**
- **MyISAM不支持外键，InnoDB支持外键**
- **MyISAM只支持表级锁，InnoDB支持行级锁和表级锁，默认是行级锁**
- **MyISAM支持全文索引，InnoDB不支持全文索引**
- **MyISAM支持没有主键的表存在，InnoDB不支持没有主键**
- **MyISAM较简单，效率上优于InnoDB，适合小型应用**
- **MyISAM使用非聚集索引，InnoDB使用聚集索引**
