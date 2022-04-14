---
title: Redis链表
date: '2022-04-14 16:43'
swiper: false
categories: 《Redis设计与实现》读书笔记
tags:
  - Redis
swiperImg: 'https://jktql.oss-cn-shanghai.aliyuncs.com/wallpaper/10.png'
img: 'https://jktql.oss-cn-shanghai.aliyuncs.com/wallpaper/10.png'
top: false
abbrlink: 4254118650
---


# Redis链表

### 链表的定义

```c
//链表节点
typedef struct listNode{
    //前置节点
    struct listNode *prev;
    //后置节点
    struct listNode *next;
    //节点的值
    void *value;
}listNode;
```

![](https://jktql.oss-cn-shanghai.aliyuncs.com/article/Redis链表/image_ni3pZqdsZ3Eev9UmyiZJCv.png)

```c
//链表
typedef struct list{
    //表头节点
    listNode *head;
    //表尾节点
    listNode *tail;
    //链表所包含的节点数量
    unsigned long len;
    //节点值复制函数
    void *(*dup)(void *ptr);
    //节点值释放函数
    void (*free)(void *ptr);
    //节点值对比函数
    int (*match)(void *ptr,void *key);
}list;
```

![](https://jktql.oss-cn-shanghai.aliyuncs.com/article/Redis链表/image_6PhNatvJakhTbvwjpUp6Lf.png)



### Redis的链表特性

**双端**：链表节点带有prev和next指针，获取前置和后置节点的复杂度都是O(1)

**无环**：表头节点的prev指针和表尾节点的next指针都指向NULL，对链表的访问以NULL为终点。 带表头指针和表尾指针 带链表长度计数器&#x20;

**头尾指针**：将程序获取头尾节点的复杂度降为O(1)

**长度计数器**：将程序获取表长的复杂度降为O(1)

**多态**：链表节点使用void\*指针来保存节点值，并且可以通过list结构的`dup、free、match`为节点值设置类型特定函数，所以链表可以用于保存各种不同类型的值

![](https://jktql.oss-cn-shanghai.aliyuncs.com/article/Redis链表/image_wdBHtNmpe2ukhXx5LGNx8L.png)
