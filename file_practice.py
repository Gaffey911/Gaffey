'''
1.B   E:\test.txt
2.默认打开模式是 r 只读
3.二进制形式
4.dump()
5.load()
6.以二进制在末尾追加写入读取
7.不关闭会占用资源并且不会保存内容
8.tell()方法
'''

#9
filename=input('请输入文件名：')
print('请输入内容，【单独输入‘w’保存并退出】')
f=open(filename,'w')
while True:
    filecontent=input()
    if filecontent!='w':
        f.write(filecontent)
    else:
        break
f.close()
#10
file=input('请输入要打开的文件：')
n=int(input('请输入需要显示几行：'))
f = open(file,'r+')
for i in f.readlines()[0:n] :
    print(i)

#11
file=input('请输入要打开的文件：')
n1=int(input('请输入开始行数：'))
n2=int(input('请输入结束行数：'))
f = open(file,'r+')
for i in f.readlines()[n1-1:n2] :
    print(i)

#12
file=input('请输入文件名：')
word1=input('请输入需要替换的单词或字符：')
word2=input('请输入新的单词或字符：')
counter=0
count=[]
f=open(file,'r')
for i in f:
    for each in i:
        if word1==each:
            counter+=1
        i=i.replace(word1,word2)
    count.append(i)
print('文件',file,'中共有',counter,'个',word1,'您确定要把所有',word1,'替换成',word2,'吗？【yes or no】')
chose=input()
if chose=='yes':
    f1=open(file,'w')
    f1.writelines(count)
    f1.close()
    f.close()
else:
    print('退出程序')
    f.close()