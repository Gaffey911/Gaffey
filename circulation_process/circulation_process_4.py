print("100以内能被3整除不能被5整除的数的和：")
sum=0
for i in range(1,100):
    if i%3==0 and i%5!=0:
        sum+=i
print(sum)
