---
title: 第3章 JDK并发包
date: '2021-07-27 21:56'
swiper: true
categories: 《Java高并发程序设计》读书笔记
tags:
  - Java并发
swiperImg: >-
  https://img14.360buyimg.com/ddimg/jfs/t1/197095/32/136/315069/6100111eEc96d1c5c/5a03f1a7eb385e9b.jpg
img: >-
  https://img14.360buyimg.com/ddimg/jfs/t1/197095/32/136/315069/6100111eEc96d1c5c/5a03f1a7eb385e9b.jpg
top: true
abbrlink: 4214418351
---

## 3.1.1 重入锁ReentrantLock和synchronized的区别
```java
public static ReentrantLock lock = new ReentrantLock();
@Override
public void run(){
	for(int i = 0;i<1000;i++){
    	lock.lock();//指定何时加锁
        try{
            i++;
        }finally{
        	lock.unlock();//指定何时解锁
        }
    }
}
```

- **ReentrantLock的特点：**
   - **在等待锁的过程中，可以中断线程让他不再等待，lock.lockInterruptibly()**
   - **可以指定公平锁或者非公平锁**
      - **公平锁的意思就是当锁可用时，先申请该锁的线程先获得锁**
   - **提供了Condition类，可以实现synchronized类似wait/notify的功能**
- **当需要使用ReentrantLock这三个特点时使用，其他时候可以使用synchronized**

---

## 3.1.3 信号量（Semaphore）

- **用来指定同时可以有多少线程访问某个资源**

---

## 3.1.4 ReadWriteLock读写锁

- **读写锁是为了防止读操作和读操作之间不阻塞，读写锁访问约束如下图所示**

**![](/medias/第3章JDK并发包/0.png)**

---

## 3.1.5 倒计时器（CountDownLatch）

- **适用场景：火箭发射**
- **主线程在CountDownLatch上等待，当所有前置任务完成后，主线程再执行**

---

## 3.2 线程池
### 首先是线程池框架：
![](/medias/第3章JDK并发包/1.png)

---

### 如何使用线程池？

- **常用的线程池**

**![](/medias/第3章JDK并发包/2.png)**

- **手动创建线程池**

**![](/medias/第3章JDK并发包/3.png)**

- **线程池实现原理**

**![](/medias/第3章JDK并发包/4.png)**

   - **即和corePoolSize、workQueue、maximumPoolSize比较**

---

## 3.3 JDK并发容器（仅了解，后续专门出专栏深入分析）

- **ConcurrentHashMap**
- **CopyOnWriteArrayList**
- **BlockingQueue**
- **ConcurrentSkipListMap**
