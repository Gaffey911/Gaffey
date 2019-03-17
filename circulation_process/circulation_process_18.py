n=int(input("请输入你需要几项："))
n1=0
n2=1
count=2
if n==1:
    print(n1)
else:
    print(n1,",",n2,end=",")
    while count<n:
        nth=n1+n2
        print(nth,end=",")
        n1=n2
        n2=nth
        count+=1
