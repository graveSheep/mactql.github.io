---
title: jk式万能回溯法
date: '2022-02-08 20:24'
swiper: false
categories: Leetcode刷题笔记
tags:
  - Leetcode
swiperImg: 'https://jktql.oss-cn-shanghai.aliyuncs.com/wallpaper/0.jpg'
img: 'https://jktql.oss-cn-shanghai.aliyuncs.com/wallpaper/0.jpg'
top: false
abbrlink: 2484785620
---


<a name="pLjmt"></a>
## 步骤：
1. **画出解空间树型图**
1. **根据经验写出dfs需要的参数**
1. **写上结束条件**
1. **根据树型图写出for循环，并与图中每一层比较是否对应**
1. **接下来套回溯模版即可**
1. **若返回值需要存入数据结构且会被回溯清空，需要另外备份一份才能存入**



<a name="wq2o1"></a>
## 使用案例1：leetcode77 组合
![](https://jktql.oss-cn-shanghai.aliyuncs.com/article/jk式万能回溯法/0.png)
<a name="jVpwE"></a>
### 配套使用方法：

1. **假设n=4，k=3，则画出树型图如下：**

![](https://jktql.oss-cn-shanghai.aliyuncs.com/article/jk式万能回溯法/1.png)

2. **思考dfs需要的参数：n，k，当前到第几个数了index，当前的临时tempList**
2. **结束条件：index到n，说明已经找到一个解了**
2. **for循环：若index=0，则从1开始，否则从上一个存入的数+1开始，一直到k结束**
<a name="sV3RT"></a>
### 代码答案：
```java
public List<List<Integer>> ans = new LinkedList<>();

public List<List<Integer>> combine(int n, int k) {
    dfs(k,0,new LinkedList<Integer>(),n);
    return ans;
}
public void dfs(int numOfList,int curindex,List<Integer> temp,int maxNum){
    if(curindex == numOfList){
        ans.add(new LinkedList<Integer>(temp));
        return;
    }
    for(int i = (temp.isEmpty() ? 1 :temp.get(curindex-1)+1);i <= maxNum;i++){
        temp.add(i);
        dfs(numOfList,curindex+1,temp,maxNum);
        temp.remove(curindex);
    }
}
```

<br />
<br />​<br />
