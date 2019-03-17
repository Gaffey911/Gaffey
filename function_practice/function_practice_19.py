def fun():
    a=int(input())
    for i in range(1,a+1):
        if a%i==0:
            print(i)
print('请输入一个整数')
fun()