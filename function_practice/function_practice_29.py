def wanquan(m):
    n=int (m**0.5)
    if n*n==m:
        return True
for abc in range(100,1000):
    for xyz in range(100,1000):
        if wanquan(abc)==True and wanquan(xyz)==True:
            a=abc//100
            b=abc//10%10
            c=abc%10
            x=xyz//100
            y=xyz//10%10
            z=xyz%10
            ax=a*10+x
            by=b*10+y
            cz=c*10+z
            if wanquan(ax)==True and wanquan(by)==True and wanquan(cz)==True:
                print(abc,xyz)