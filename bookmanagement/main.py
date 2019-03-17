import sys
books=[['001','确认过眼神，我就是这么优秀的人','左手韩',90],['002','老马','左手韩',85],['003','如果能重来，我想做熊孩','左手韩',80]]
users=[['Gaffey','123456'],['hyb','147258']]
flag=True
flag1=True
while flag==True:
    print('**********************')
    print('*欢迎来到图书管理系统*')
    print('**********************')
    print('1.登录 2.注册 3.退出')
    n=int(input("请输入对应的数字："))
    if n==1:
        print('请输入用户名：', end='')
        username = input()
        print('请输入用户密码：', end='')
        password = input()
        if [username, password] in users:
            print('登录成功！')
            flag=False
            while flag1==True:
                print('**********************')
                print('*欢迎来到管理界面*')
                print('**********************')
                print('1.查看所有书籍 2.增加书籍 3.删除书籍 4.查找书籍 5.修改书籍 6.退出系统')
                m=int(input("请输入对应的数字："))
                if m==1:
                    print( )
                    for i in books:
                        print('编号',i[0],'书名:',i[1],  '作者:',i[2], '价格:', i[3])
                    print()
                elif m==2:
                    booknum=input('请输入编号:')
                    bookname=input('请输入书名：')
                    author=input('请输入作者：')
                    price=int(input('请输入价格：'))
                    books.append([booknum,bookname, author, price])
                    print('\n添加书籍成功！')
                    print('现在书库中书籍有：')
                    for i in books:
                        print('编号',i[0],'书名:', i[1], '作者:', i[2], '价格:', i[3])
                    print()
                elif m==3:
                    booknum = input('请输入编号:')
                    for i in books:
                        if i[0]==booknum:
                            print('您要删除的书籍为：')
                            print('编号', i[0], '书名:', i[1], '作者:', i[2], '价格:', i[2])
                            list=[i[0],i[1],i[2],i[3]]
                            books.remove(list)
                            print('删除书籍成功')
                            print('现在书库中书籍有：')
                            for i in books:
                                print('编号',i[0],'书名:', i[1], '作者:', i[2], '价格:', i[2])

                        else:
                            print('无法查询到此书籍')
                elif m==4:
                    booknum= input('请输入编号：')
                    for i in books:
                        if i[0] == booknum:
                            print('编号',i[0],'书名:', i[1], '作者:', i[2], '价格:', i[3])
                        else:
                            print('无法查询到此书籍')
                elif m==5:
                    booknum= input('请输入编号：')
                    for i in books:
                        if i[0] == booknum:
                            print('您要修改的书籍为：')
                            print('编号', i[0], '书名:', i[1], '作者:', i[2], '价格:', i[3])
                            list = [i[0], i[1], i[2], i[3]]
                            books.remove(list)
                            print('请选择您要修改的内容 1.书名 2.作者 3.价格')
                            k  = int(input("请输入对应的数字："))
                            if k==1:
                                bookname=input('请输入书名：')
                                list[1]=bookname
                                books.append(list)
                            elif k==2:
                                author = input('请输入作者：')
                                list[2]=author
                                books.append(list)
                            elif k==3:
                                price = int(input('请输入价格：'))
                                list[3]=price
                                books.append(list)
                            print('修改成功')
                        else:
                            print('无法查询到此书籍')
                    print('现在书库中书籍有：')
                    for i in books:
                        print('编号', i[0], '书名:', i[1], '作者:', i[2], '价格:', i[3])
                elif m==6:
                    sys.exit(0)

        else:
            print('\n用户名不存在或密码错误,请重新登录或注册')
    elif n==2:
        username = input('请输入用户名：')
        password = input('请输入用户密码：')
        users.append([username, password])
        print('注册成功！')
    elif n==3:
        sys.exit(0)

