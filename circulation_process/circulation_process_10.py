for i in range(1000,10000):
    a=int(str(i)[0])
    b=int(str(i)[1])
    c=int(str(i)[2])
    d=int(str(i)[3])
    if (a*10+b+c*10+d)**2==i:
        print(i)