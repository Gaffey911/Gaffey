def zhishu():
    n=int(input('请输入一个大于6的偶数'))
    if n%2==0 and n>6:
        for i in range(0,int(n/2)):
            if i%2!=0:
                j=n-i
                print(i,'+',j,'=',n)
    else:
        print('输入有误')

zhishu()