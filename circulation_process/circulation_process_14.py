a=int(input("请输入一个整数"))
sum=0
while a!=0:
    t=a%10
    a=a//10
    sum=sum+t
print(sum)