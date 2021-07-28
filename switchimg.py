import os
import re
import requests

class mdrebug:
    sums = 0
    org=''
    par=''
    datas=[]
    def func(self,x):
        l = x.group()
        s=self.org.replace(l, r'(/medias/'+self.par+'/'+str(self.sums)+r'.png)')
        self.org=s
        self.sums += 1
    def modify_md_content(self,top):
        with open(top) as fr:
            data = fr.read()
            self.org=data
            data = re.sub(r'\(http.+\)', lambda x: self.func(x), data)
    def downloadimg(self,top):
        with open(top) as fr:
            data = fr.read()
            self.org=data
            self.datas = re.findall(r'(?:\()(http.+?\.png)',data)
            print('正在下载呢急个p')

if __name__ == '__main__':

    truetittle = r'第4章锁的优化'

    filepath = r'/Users/caiyiming/myblog/themes/mytheme/source/medias/'
    workpath=r'/Users/caiyiming/myblog/source/_posts/'

    top = truetittle + r'.md'
    ts = mdrebug()
    ts.par = top[:-3]
    mediapath = filepath + ts.par+'/'
    ts.downloadimg(workpath + top)
    isExists = os.path.exists(mediapath)
    if not isExists:
        os.makedirs(mediapath)
    sum=0
    for x in ts.datas:
        r = requests.get(x)
        with open(mediapath+str(sum)+'.png','wb') as f:
            f.write(r.content)
            sum+=1
    isExists1 = os.path.exists(workpath + top)
    if isExists1:
        ts.modify_md_content(workpath + top)
        ans = ts.org.replace(r'![image.png]', r'![]')
        os.remove(workpath + top)
        fo = open(workpath + top, "w")
        fo.write(ans)
    print('整好了')
