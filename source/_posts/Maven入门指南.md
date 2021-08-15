---
title: Maven入门指南
date: '2021-08-14 11:35'
swiper: false
categories: 《Maven项目管理》课程笔记
tags:
  - Maven
swiperImg: >-
  https://img13.360buyimg.com/ddimg/jfs/t1/189988/19/17886/929288/61173a8eE22927680/ff1fd68f1eb8f510.png
img: >-
  https://img13.360buyimg.com/ddimg/jfs/t1/189988/19/17886/929288/61173a8eE22927680/ff1fd68f1eb8f510.png
top: false
abbrlink: 477950076
---

## 为什么要用Maven？
- **场景一：idea开发的项目没法到eclipse中运行，即不同的ide开发的项目不能互相使用**
- **场景二：大型项目需要很多个jar包，要去不同的网站下载，也不方便更新，很麻烦**

---

## IDEA上怎么创建Maven项目？
**创建Maven项目时需要填写以下信息**

- **GroupID：机构名或者逆向域名的形式**
- **ArtifactID：项目名称**
- **Version：版本号**

**创建好了以后会自动生成Maven项目结构以及配置文件pom.xml**

---

## Maven项目结构是什么样的？
![](/medias/Maven入门指南/0.png)

---

## 那pom.xml文件是干啥的？
**pom.xml文件是用来配置项目依赖的，Maven会通过这些依赖自动下载第三方组件**
## 那么怎么在pom.xml中配置项目依赖呢？
**在search.maven.org网站中搜索需要的组件，找到需要的组件的依赖后加入pom.xml的`<dependencies></dependencies>`中，然后maven就会自动下载这些组件了**

---

## 怎么让maven下载依赖的速度快一点呢？
**Maven首先去本地仓库找，如果本地仓库没有再去中央仓库下载到本地仓库。**
**为了加快下载速度，可以使用私服，从私服下载到本地仓库**
```xml
<!-- 可以在pom.xml的<version>下方添加一个阿里云私服的地址配置 -->
<repositories>
  <repository>
    <id>aliyun</id>
    <name>aliyun</name>
    <url>https://maven.aliyun.com/repository/public</url>
  </repository>
</repositories>
```

---

## maven命令常用的有哪些？

- **compile：编译，编译成功后会增加一个target目录**
- **clean：删除整个target目录**
- **test：在集成junit，并且有test项目和测试类**
- **package：把项目打包成jar包**
- **install：把打好的jar包放到本地仓库去**
