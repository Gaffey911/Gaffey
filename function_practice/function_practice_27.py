def jiecheng(n):
    if n == 1:
        return 1
    elif n > 1:
        return n *jiecheng(n - 1)
for i in range(100,1000):
    a=i//100
    b=i//10%10
    c=i%10
    if i==jiecheng(a)+jiecheng(b)+jiecheng(c):
        print(i)