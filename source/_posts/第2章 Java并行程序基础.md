---
title: 第2章 Java并行程序基础
date: '2021-07-08 15:27'
swiper: false
categories: 《Java高并发程序设计》读书笔记
tags:
  - Java并发
swiperImg: >-
  https://img11.360buyimg.com/ddimg/jfs/t1/195850/7/2628/664921/609b613fE9b7a2cac/9a03fb980c5fc2c6.jpg
img: >-
  https://img11.360buyimg.com/ddimg/jfs/t1/195850/7/2628/664921/609b613fE9b7a2cac/9a03fb980c5fc2c6.jpg
top: false
abbrlink: 1877506347
---

## 2.1 进程和线程
- **进程是独立运行、资源分配的基本单位，程序运行起来就是进程**
- **线程是资源调度的基本单位，一个进程可以有多个线程**

### 线程的生命周期如下：
**![](https://img14.360buyimg.com/ddimg/jfs/t1/183619/38/12549/74295/60e2632cEb819b275/319a62e48ed7704f.jpg)**
> - **New状态表示刚刚创建的线程，还没开始执行，要start（）方法调用后才执行**
> - **线程执行时是RUNNABLE状态，表示一切资源都准备好了**
> - **如果遇到synchronized同步块，则会被阻塞BLOCKED**
> - **当线程中调用wait、join方法时，当前线程就会进入等待态WAITING，等待notify方法唤醒**
> - **当线程中调用wait(time)等方法时，当前线程就会进入有限时间等待态TIMED_WAITING**
> - **线程执行完毕后，就会进入TEAMINATED态**


---

## 新建线程的方法：

- **参考文献：[创建线程的方法](https://zhuanlan.zhihu.com/p/144694652)**
- **本质是两种方法**
   - **继承 Thread 类 或者直接 匿名内部类**
   - **实现 Runnable 接口**
- **还有其他很多表现形式，但本质都是上面两种**
   - **通过 ExecutorService 和 Callable 实现有返回值的线程 (这里仅作了解)**
   - **基于线程池的execute()，创建临时线程 (这里仅作了解)**

### 继承Thread类
```java
//创建线程类
public class ThreadDemo extends Thread {
    //重写run()方法
    @Override
    public void run() {
        ...
    }
}
//创建线程对象
ThreadDemo t1 = new ThreadDemo();

//启动线程
t1.start();
```

### 实现 Runnable 接口
```java
//实现Runnable 接口创建线程类 ThreadDemo
public class ThreadDemo implements Runnable {
    @Override
    //重写run()方法
    public void run() {
        ...
    }
}

//创建线程对象,传入Runnable实现类实例
Thread t1 = new Thread(new ThreadDemo());

//启动线程
t1.start();
```

### **通过 ExecutorService 和 Callable 实现有返回值的线程**

- **我们需要在主线程中开启多个线程去执行一个任务，然后收集各个线程的返回结果并将最终结果进行汇总，这时就需要用到 Callable 接口**
- **如果不需要返回值，仍然可以用Runnable**
- **线程的返回结果为Future对象，isDone方法判断线程是否完成，get方法获取结果**
```java
//通过实现Callable接口来创建线程类
public class CThread implements Callable<String> {
    private String name;

    public CThread(String name ) {
        this.name = name;
    }

    //重写call()方法
    @Override
    public String call() throws Exception {
        return name;
    }   
}

//创建线程池
ExecutorService pool = Executors.newFixedThreadPool(5);

//创建接收结果的列表集合
List<Future> list = new ArrayList<Future>();

for(int i = 0;i<5;i++) {
    //创建线程对象
    Callable c = new CThread("线程"+i);

    //将线程对象提交到线程池中，并将返回结果接收
    Future future = pool.submit(c);
    System.out.println("线程"+i+"已经加入线程池");

    //将返回结果加入集合
    list.add(future);
}

//关闭线程池
pool.shutdown();

//打印返回结果
for (Future future : list) {
    try {
        System.out.println(future.get().toString());
    } catch (InterruptedException | ExecutionException e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
    }
}
```

---

### 启动线程：
> - **start方法是新建线程并启动线程**
> - **run方法是启动当前线程，不会开启新线程**


---

## 线程终止和中断

- **终止线程不要用stop方法，会出现数据不一致问题**
- **线程中断的方法：**
   - **用interrupt，并且在while循环中通过if判断中断标志位即可**
   - **Thread.sleep(time)，让线程休眠**
```java
public void run(){
	while (true) {
        // 响应中断
        if (Thread.currentThread().isInterrupted()) {
            System.out.println("线程被中断。");
            break;
        }
        Thread.yield();
    }
}
```



---

## 2.3 初识volatile
> **作用：**
> - **volatile是同步机制。读volatile变量之前，会让本地缓存失效，必须去主存中读最新值。写volatile变量会直接刷新到主存**
> - **volatile可以禁止指令重排**
> **缺点：不能保证i++的原子性**

---

## 2.5 守护线程

- **在线程start之前，setDaemon(true)方法可以设置守护线程**
- **守护线程会在父线程结束后自动结束**

---

## 2.7 初识synchronized
### synchronized的作用：
> - **和volatile一样都是为了实现线程安全，但是volatile不能真正做到线程安全，因为不能保证原子性**
> - **于是就有了synchronzied，用来实现线程同步。会对同步的代码加锁，只允许一个线程进入同步块**

### synchronized怎么用？

- **synchronized有三种用法：**
   - **给对象加锁:**
```java
@Override
public void run() {
    synchronized (object) {
        ...
    }
}
```

   - **给实例非静态方法加锁**
```java
public synchronized void fun(){...}
@Override
public void run() {
    fun(); //在run方法内部调用synchronized非静态方法
}
```

   - **给静态方法加锁**
```java
public static synchronized void fun(){...}
@Override
public void run() {
    fun(); //在run方法内部调用synchronized静态方法
}
```

- **synchrozied三种用法总结：**
   - **对象锁和非静态方法都要用同一个Runnable实例创建线程，这样对同一个实例对象加锁，才能实现多线程的同步**
   - **静态方法实际上是对类加锁，所以即使是不同的Runnable实例，只要是同一个类，即可完成线程同步**
