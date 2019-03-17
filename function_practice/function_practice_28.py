def jiaogu(x):
    while x>1:
        if x%2==0:
            x=x/2
            print('偶数，除以二为',x)
        else:
            x=x*3+1
            print('奇数，乘三减一为',x)
    return x

a=int(input('输入自然数:'))
print(jiaogu(a))