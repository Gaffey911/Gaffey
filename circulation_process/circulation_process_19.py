n=int(input("请输入整数"))
count=0
while n>0:
    if n%2==1:
       count+=1
    n=n//2
print("总共有",count,"位1")