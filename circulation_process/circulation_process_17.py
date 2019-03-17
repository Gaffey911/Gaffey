pi=0.0
a=1
t=0
while  pi<3.1415926 :
    pi+=4/a
    if a<0:
        a-=2
    else:
        a+=2
    a=-a
    t+=t
print(t)