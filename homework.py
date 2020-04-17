# -*- coding:utf-8 -*-
## 1.读取文件
with open('q:/python/classroom/scores.txt',encoding='utf-8') as f:
    l=f.readlines()
    print(l)
#将每一行数据都作为一个字符串存储到集合l中
    a=[]
for i in l:
    b=i.split()
    a.append(b)
a[0].append('总分')
a[0].append('平均分')
#新知识！可以利用集合中的子集合更改数据
#将每一个字符串的内容以空格为切割符转换为列表，现在大集合为a

## 2.统计每一名学生的总成绩、平均值和从高到低排序
for i in a[1:]:
    #i是一个列表，a的子列表
    sum=0
    for n in i[1:]:
        N=int(n)
        sum=sum+N
        #这个地方要用循环加
    i.append(str(sum))
    average=sum//len(i[1:])
    i.append(str(average))
a.sort(key=lambda x:x[10],reverse=True )
#新知识！如果a是一个由元祖/列表组成的列表，对该列表排序时，需要用到sort的参数key,用来指定排序的关键词。lambda是一个匿名函数，是固定写法；x表示匿名函数的输入，即列表中的一个元素，在这里，表示一个元组，x只是临时起的一个名字，你可以使用任意的名字；x[0]表示匿名函数的输出，即元组里的第一个元素，即key = x[0]；所以这句命令的意思就是按照列表中第一个元素进行排序

## 3. 汇总每一科目的平均分和总平均分
#这一个要多看看，好绕
x=len(i[1:])
y=len(a[1:])
xiangjia=[]
xiangchu=[]
for j in range(x):
    xiangjia.append(0)
    xiangchu.append(0)
for i in a[1:]:
    fenshu=i[1:]
    for num in range(x):
        fenshu1=int(fenshu[num])
        xiangjia1=int(xiangjia[num])
        xiangjia[num]=fenshu1+xiangjia1
for num in range(x):
    m=int(xiangjia[num])
    xiangchu[num]=m//y
xiangchu.insert(0,'平均')
a.insert(1,xiangchu)

## 4.为学生加上名次
a[0].insert(0,'名次')
a[1].insert(0,'0')
mingci=0
for i in a[2:]:
    mingci=mingci+1
    i.insert(0,str(mingci))
print(a)


## 5.替换60分以下的成绩为“不合格”
for list in a[2:]:
    for m in range(2,10):
        if float(list[m])< 60:
            list[m]="不合格"
#这个地方一开始写的如下，为什么不可以成功替换呢？
#for list in a[2:]:
#   for m in list[2:]:
#        if float(m)<60:
#            m=m.replace(m,'不合格')
print(a)


## 6.存储成新文件
#这里注意嵌套关系不仅是内外层的关系，注意最内层的处理方式也会影响外层，所以最后用write而不是writelines.
with open('result.txt','w') as f:
    for list in a:
        for i in list:
            f.write(str(i)+'\t')
        f.write('\n')
