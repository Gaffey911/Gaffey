import operator
import pickle

def regist(username,userpwd):

    usermoney=0.0
    users.append([username,userpwd,usermoney])
    info = open('user.txt', 'wb')
    pickle.dump(users, info)
    print('注册成功！用户名:',username,'余额:',usermoney)
    return users
def login(users):
    name=input('请输入用户名:')

    for i in users:
        if name==i[0]:
            pwd = input('请输入密码:')
            if pwd==i[1]:
                print('登陆成功')
                return name,True
            else:
                print('密码错误')
                return name,False



def addMoney(l):
    name=input('请输入用户名:')
    for i in l:
        if name==i[0] :

            money=int(input('用户存在，请输入存款金额:'))
            i[2]+=money
            print('充值成功，余额为:',i[2])
            return True


    f=open('user.txt','wb')
    pickle.dump(l,f)
def lookBang():
    f=open('books.txt','rb')
    l=pickle.load(f)
    print('*******推荐榜*******')
    l.sort(key=operator.itemgetter(2),reverse=True)
    for i in l:
        print('《',i[1],'》','推荐数：',i[2])
    print('*******打赏榜*******')
    l.sort(key=operator.itemgetter(3),reverse=True)
    for i in l:
        print('《',i[1],'》','打赏数：',i[3])
    print('*******点击榜******')
    l.sort(key=operator.itemgetter(4),reverse=True)
    for i in l:
        print('《',i[1],'》','点击数：',i[4])
def reading(l,name):
    flag3 = True

    a=input('请输入编号：')
    for i in l:
        if a==i[0]:
            i[4]+=1
            f=open(i[1],'r')
            lr = f.readlines()
            n=10
            for i in lr[0:n]:
                print(i)

            while flag3:
                print('1.推荐','2.打赏','3.下一页（扣余额）','4.上一页','0.退出')
                x=input('请输入相应操作：')
                if x=='1':
                    i[2]+=1
                elif x=='2':
                    b=lessMoney(name)
                    if b==True:
                        i[3]+=1
                    elif b==False:
                        print('余额不足')
                        flag3=False
                        global flag1
                        flag1=True
                elif x=='3':
                    a=lessMoney(name)
                    if a==True:
                        print('************************************')
                        for i in lr[n:n+10]:
                            print(i)
                        n=n+10
                    elif a==False:
                        flag3=False
                        global flag1
                        flag1 = True
                elif x=='4':
                    for i in lr[n-20:n-10]:
                        print(i)
                    n=n-10
                elif x=='0':
                    flag3=False
    fb = open('books.txt', 'wb')
    pickle.dump(l, fb)
    fb.close()
    return flag3
def lessMoney(name):
    f = open('user.txt', 'rb')
    l = pickle.load(f)
    for i in l:
        if i[0] == name:
            if i[2]>1:
                i[2] = i[2] - 1
                print('扣款成功，余额为：', i[2])
                return True
            elif i[2]<1:
                print('余额不足，请充值')
                return False

    f=open('user.txt','wb')
    pickle.dump(l,f)
    f.close()


users=[['zqy','123456',0.0],['hyb','123456',0.0]]
books=[['001','极道天魔',0,0,0],['002','剑动星穹',0,0,0],['003','恰与暴君共枕眠',0,0,0],['004','都市大亨',0,0,0]]

flag1=True
flag2=True
flag3=True
while flag1==True:
    print('————————欢迎来到小说世界————————')
    print('1.注册','2.登录看书','3.充值','4.查看榜单','0.退出')
    a=input('输入编号：')
    if a=='1':
        f = open('user.txt', 'rb')
        l = pickle.load(f)
        username = input('请输入用户名:')
        for i in l:
            if username in i :
                print('用户名存在，请重新输入')
                username=input('请输入用户名:')
        userpwd = input('请输入密码:')
        regist(username,userpwd)
        flag1=True
        f.close()
    elif a=='2':
        f = open('user.txt', 'rb')
        l = pickle.load(f)
        t=login(l)
        if t[1]==True:
            flag1=False
            while flag2==True:
                fb=open('books.txt','rb')
                lb=pickle.load(fb)
                print('欢迎您',t[0])
                print('1.古典仙侠', '2.东玄西幻', '3.霸道总裁', '4.都市人生', '0.退出')
                b=input('输入编号：')
                if b=='1':
                    flag2=False
                    print('*********古典仙侠*********')
                    print(lb[0][0],'书名:',lb[0][1],'推荐:',lb[0][2],'打赏:',lb[0][3])
                    a=reading(lb,t[0])

                elif b=='2':
                    flag2 = False
                    print('*********东玄西幻*********')
                    print(lb[1][0], '书名:', lb[1][1], '推荐:', lb[1][2], '打赏:', lb[1][3])
                    b=reading(lb,t[0])

                elif b=='3':
                    flag2 = False
                    print('*********霸道总裁*********')
                    print(lb[2][0], '书名:', lb[2][1], '推荐:', lb[2][2], '打赏:', lb[2][3])
                    c=reading(lb,t[0])

                elif b=='4':
                    flag2 = False
                    print('*********都市人生*********')
                    print(lb[3][0], '书名:', lb[3][1], '推荐:', lb[3][2], '打赏:', lb[3][3])
                    d=reading(lb,t[0])

                elif b=='0':
                    flag2=False
                    flag1=True

        elif t[1]==False:
            flag1=True
    elif a=='3':
        f = open('user.txt', 'rb')
        l = pickle.load(f)
        addMoney(l)
        f.close()
    elif a=='4':
       lookBang()
    elif a=='0':
        exit(0)

