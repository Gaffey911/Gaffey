def yinzi(a):
    sum=0
    for i in range(1,int(a/2+1)):
        if a%i==0:
            sum+=i
    return sum
def qinmi():
    for x in range(0,3000):
        y=yinzi(x)
        if x==yinzi(y) and x<y:
            print(x,y)
qinmi()