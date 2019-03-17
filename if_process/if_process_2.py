a=int(input('请输入第一个数'))
b=int(input('请输入第二个数'))
c=int(input('请输入第三个数'))
if a>b:
    max=a
else:
    max=b
if c>max:
    print('最大数',c)
else:
    print('最大数',max)