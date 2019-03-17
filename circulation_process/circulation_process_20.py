year=int(input("请输入年份"))
month=int(input("请输入月份"))
day=int(input("请输入日子"))
sum=0
i=2000
j=1
k=1
while i<year:
    if i%4==0 and i%100==0 or i%400==0:
        sum+=366
    else:
        sum+=365
    i+=1
while j<month:
    if j==4 or 6 or 9 or 11:
        sum+=30
    elif j==2:
        if year%4==0 and year%100==0 or year%400==0:
            sum+=29
        else:
            sum+=28
    else:
        sum+=31
    j+=1
sum+=day
if sum%5==4 or 0:
    print("晒网")
elif sum%5==1 or 2 or 3:
    print("打渔")