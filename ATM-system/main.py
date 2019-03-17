import random
accounts=[['zqy','123456',100001,10000.0],['hyb','123456',100002,10000.0]]
def regist():
    rusername=input('请输入用户名：')
    rpassword=input('请输入密码：')
    raccount=str(random.randint(100003,1000000))
    rmoney=0.0
    accounts.append([rusername,rpassword,raccount,rmoney])
    print('注册成功，您的用户名为：',rusername,'账号为：',raccount,'当前账户余额0元')
    return accounts
def login():
    uaccount = int(input('请输入账号：'))
    upassword = input('请输入密码：')
    for i in accounts:
        if uaccount in i:
            i[1]==upassword
            return uaccount,True
        else:
            print('\n账号不存在或密码错误,请重新登录或注册')
            return uaccount,False
def search(uaccount):
    for i in accounts:
        if i[2]==uaccount:
            print('余额为:',i[3])
def withdrawMoney(uaccount):
    withM=int(input('请输入取款金额：'))
    for i in accounts:
        if i[2]==uaccount:
            if i[3]>withM:
                i[3]=i[3]-withM
                print('取款成功，您的余额还有',i[3],'元')
            else:
                print('余额不足，不能取款')
def deposit(uaccount):
    deM = int(input('请输入存款金额：'))
    for i in accounts:
        if i[2] == uaccount:
            i[3] = i[3] + deM
            print('存款成功，您的余额还有', i[3], '元')
def zhuanzhang(uaccount,zaccount):
    for i in accounts:
        if i[2]==zaccount:
            print('账户存在')
            zhuanM=int(input('请输入转账金额：'))
            for j in accounts:
                if j[2]==uaccount and j[3]>zhuanM:
                    j[3]-=zhuanM
                    print('扣款成功')
                else:print('扣款失败')
            i[3]+=zhuanM
            print('转账成功')
        else:print('账户不存在！')
def changePsw(account):
    oldPsw=input('请输入旧密码：')
    newPsw=input('请输入新密码：')
    newPsw1=input('请再次输入新密码：')
    if newPsw == newPsw1:
        for i in accounts:
            if i[2] == account:
                print('账户存在')
                if i[1] == oldPsw:
                    i[1] = newPsw
                    print('修改成功')
                else:
                    print('旧密码输入错误')
    else:
        print('两次输入不一致，请检查后输入')

def exit():
    print('谢谢，欢迎下次再来')

flag = True
flag1 = True
while flag==True:
        print('**********************')
        print('*欢迎来到自动提款机系统*')
        print('**********************')
        print('1.注册  2.登录')
        m=int(input("请输入对应的数字："))
        if m==1:
            regist()
        elif m==2:

                t=login()
                if t[1]==True:
                    flag=False
                    while flag1 == True:
                        print('**********************')
                        print('*欢迎来到操作界面*')
                        print('**********************')
                        print('1.查询余额 2.取款 3.存款 4.转账 5.改密 0.退出')
                        n = int(input("请输入对应的数字："))
                        if n==1:
                            search(t[0])
                        elif n==2:
                            withdrawMoney(t[0])
                        elif n==3:
                            deposit(t[0])
                        elif n==4:
                            zhuanAccount = input('请输入对方账号')
                            zhuanzhang(t[0],zhuanAccount)
                        elif n==5:
                            changePsw(t[0])

                        elif n==0:
                            exit()
                        else:
                            print('输错了，不要急！')
                            flag1=True
                elif t[1]==False:
                   flag=True

        else:
            print('输错了，不要急！')
            flag=True









