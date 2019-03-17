import random
print(''' *******欢迎来到猜拳游戏*********
 *******让我们一局定输赢********
 ************游戏规则************
 *****0-剪刀  1-石头  2-布*****
 ************开始PK吧***********''')
user=input("请输入对应数字：")
userNum=int(user)
num=random.randint(0,2)

if userNum==0:
    print("你出的是剪刀")
elif userNum==1:
    print("你出的是石头")
elif userNum==2:
    print("你出的是布")

if num == 0:
    print("电脑出的是剪刀")
elif num == 1:
    print("电脑出的是石头")
elif num == 2:
    print("电脑出的是布")


if (userNum==0 and num==2) or (userNum==1 and num==0) or (userNum==2 and num==1):
    print("你赢啦")
elif userNum==num:
    print("平局")
else:
    print("电脑赢啦")
