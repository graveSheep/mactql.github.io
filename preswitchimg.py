import os
import re
import requests
from PIL import Image

class mdrebug:
    sums = 0
    org=''
    par=''
    datas=[]
    def func(self,x):
        l = x.group()
        s=self.org.replace(l, r'(https://jktql.oss-cn-shanghai.aliyuncs.com/article/'+self.par+'/'+str(self.sums)+r'.png)')
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
    file_name = input("输入文件名: ");
    truetittle = file_name

    filepath = r'/Users/caiyiming/Downloads/'
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


# print('正在缩小图片呢急个p')
# for i in range(0,sum):
#     # 打开图片
#     image = Image.open(mediapath+str(i)+'.png')
#     # 缩小
#     # 图片对象.thumbnail(大小) - 按比例缩放
#     image_w, image_h = image.size
#     if image_h < 500:
#         continue
#     elif image_h > 750:
#         image.thumbnail((image_w/2, image_h/2))
#     else:
#         image.thumbnail((image_w/1.5, image_h/1.5))
#     os.remove(mediapath+str(i)+'.png')
#     # image.show()
#     image.save(mediapath+str(i)+'.png')
#     i+=1

print('整好了')
