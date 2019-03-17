num = int(input("请输入一个数字: "))
nums=int(num**0.5)
for i in range(2,nums+1):
    if num<=1:
        print("既不是质数，又不是合数")
    if num%i==0:
        print(num,'不是质数')
    else:
        print(num,'是质数')