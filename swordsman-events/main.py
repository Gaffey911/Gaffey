import random,sys,time,mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="db"
)
mycursor = mydb.cursor()

class Role(object):
    def __init__(self,name,life,damage,level):
        self.name=name
        self.life = life
        self.damage=damage
        self.level=level
    def getName(self):
        return self.name
    def getLife(self):
        return self.life
    def getDamage(self):
        return self.damage
    def getLevle(self):
        return self.level

class Knife(Role):
    def attack(self,enemy):

        print('******************************')
        move=random.choice((1,2,3))
        if move==1:
            print(self.getName(),'使出乌鸦坐飞机，迅速攻击',enemy.getName())
        elif move==2:
            print(self.getName(),'以气化形，使出刀雨梨花，刺向',enemy.getName())
        elif move==3:
            print(self.getName(),'使出灭世刀法，重击',enemy.getName())
        print('造成',self.getDamage(),'点伤害')
        print(enemy.getName(),'剩余血量',enemy.getLife()-self.getDamage())
        enemy.life=enemy.getLife()-self.getDamage()

class Sword(Role):
    def attack(self,enemy):

        rate=random.randint(1,100)
        if rate>=0 and rate<=25:
            print('******************************')
            print('打出了暴击')
            move=random.choice((1,2,3))
            if move==1:
                print(self.getName(),'使出屠龙剑，迅速攻击',enemy.getName())
            elif move==2:
                print(self.getName(),'使出剑舞海棠，刺向',enemy.getName())
            elif move==3:
                print(self.getName(),'使出绝世剑法，重击',enemy.getName())
            print('造成',self.getDamage()*2,'点伤害')
            print(enemy.getName(),'剩余血量',enemy.getLife()-self.getDamage()*2)
            enemy.life=enemy.getLife()-self.getDamage()*2
        else:
            print('******************************')
            move = random.choice((1, 2, 3))
            if move == 1:
                print(self.getName(), '使出屠龙剑，迅速攻击', enemy.getName())
            elif move == 2:
                print(self.getName(), '使出剑舞海棠，刺向', enemy.getName())
            elif move == 3:
                print(self.getName(), '使出绝世剑法，重击', enemy.getName())
            print('造成', self.getDamage(), '点伤害')
            print(enemy.getName(), '剩余血量', enemy.getLife() - self.getDamage() )
            enemy.life = enemy.getLife() - self.getDamage()
class Thief(Role):
    def attack(self,enemy):
        rate=random.randint(1,100)
        if rate>=0 and rate<=25:
            print('******************************')
            print('打出了3倍暴击')
            move=random.choice((1,2,3))
            if move==1:
                print(self.getName(),'使出偷心大法，迅速攻击',enemy.getName())
            elif move==2:
                print(self.getName(),'使出巴啦啦魔仙变，刺向',enemy.getName())
            elif move==3:
                print(self.getName(),'使出行窃预兆，重击',enemy.getName())
            print('造成',self.getDamage()*3,'点伤害')
            print(enemy.getName(),'剩余血量',enemy.getLife()-self.getDamage()*3)
            enemy.life=enemy.getLife()-self.getDamage()*3
        else:
            print('******************************')
            move = random.choice((1, 2, 3))
            if move == 1:
                print(self.getName(), '使出偷心大法，迅速攻击', enemy.getName())
            elif move == 2:
                print(self.getName(), '使出巴啦啦魔仙变，刺向', enemy.getName())
            elif move == 3:
                print(self.getName(), '使出行窃预兆，重击', enemy.getName())
            print('造成', self.getDamage(), '点伤害')
            print(enemy.getName(), '剩余血量', enemy.getLife() - self.getDamage() )
            enemy.life = enemy.getLife() - self.getDamage()
def content(me):
    list=['你好','你不好','你非常好','你好呀','嘿嘿','哈哈','嘎嘎']
    flag2=True
    while flag2==True:

        print('欢迎进入游戏大厅: 1.开始决斗 2.与电脑聊两句先 3.退出')
        c=input('请输入你的选择：')
        computer = Sword('步惊云', 100, 20, 1)
        mname = me.getName()
        sql = "SELECT  name,life,damage,levle FROM sites WHERE name='" + mname + "'"
        mycursor.execute(sql)
        results = mycursor.fetchone()
        xlife = results[1]
        xdamage = results[2]
        xlevel = results[3]
        if xlife==120:
            role=Knife(xname,xlife,xdamage,xlevel)
        elif xlife==100:
            role=Sword(xname,xlife,xdamage,xlevel)
        elif xlife==80:
            role=Thief(xname,xlife,xdamage,xlevel)

        if c=='1':
            print('电脑角色为：剑客步惊云，生命值100，伤害20')

            print('您的角色为：', mname, '生命值：', xlife, '伤害：', xdamage, '等级', xlevel)
            print('决斗开始！')
            while True:
                role.attack(computer)
                if computer.getLife()<=0:
                    mlevel=role.getLevle()+1
                    mdamage=role.getDamage()+10
                    sql="UPDATE sites SET damage=%s,levle=%s WHERE damage=%s and levle=%s"
                    na=(mdamage,mlevel,role.getDamage(),role.getLevle())
                    mycursor.execute(sql,na)
                    mydb.commit()
                    print('你赢了！伤害加10，等级加1')
                    break
                time.sleep(1)
                computer.attack(role)
                if role.getLife()<=0:
                    print('步惊云赢了！')
                    i=input('你想通过解谜来增强你的实力吗？y/n：')
                    if i=='y':
                        print("答对这个问题 攻击力 +10 ")
                        a = random.randint(1, 100)
                        b = random.randint(1, 100)
                        c = a + b
                        ee = input("请问%d+%d等于多少:" % (a, b))
                        ee = int(ee)
                        if ee == c:
                            print("答对了！攻击力增加10点！")
                            newdamage=me.getDamage()+10
                            print("现在 你的攻击力是 %d " % (newdamage))
                            sql = "UPDATE sites SET damage=%s WHERE damage=%s "
                            na = (newdamage,role.getDamage())
                            mycursor.execute(sql, na)
                            mydb.commit()
                        else:
                            print("答错了！很遗憾你失去了变强的机会！")
                    break
                time.sleep(1)
        elif c=='2':
            count=0
            while count<3:
                speak=random.randint(0,6)
                print('步惊云：',list[speak])
                count+=1
        elif c=='3':
            flag2=False
            global flag1
            flag1=True



flag1=True
while flag1==True:
    print('*****欢迎来到武侠世界*****')
    print('1.创建角色 2.已有角色 3.退出')
    a=input('请输入你的选择:')

    if a=='1':
        print('请选择职业:')
        print('1.刀客（伤害少血量多）2.剑客（伤害正常血量正常，有几率两倍暴击）3.女贼（伤害高血量少，有几率3倍暴击）')
        b=input('请输入你的选择:')
        if b=='1':

            print('你选择了刀客')
            name=input('请为你的角色起一个名字:')
            knife=Knife(name,120,random.randint(10,20),1)
            sql = "INSERT INTO sites(name,life,damage,levle) value (%s,%s,%s,%s)"
            val = (knife.getName(), knife.getLife(), knife.getDamage(), 1)
            mycursor.execute(sql, val)
            mydb.commit()
            print('角色创建成功！英雄名字:', knife.getName(), '血量:', knife.getLife(), '伤害:', knife.getDamage(),'等级：1')
            content(knife)

        elif b=='2':

            print('你选择了剑客')
            name = input('请为你的角色起一个名字:')
            sword = Sword(name, 100, random.randint(20,30),1)
            sql = "INSERT INTO sites(name,life,damage,levle) value (%s,%s,%s,%s)"
            val = (sword.getName(), sword.getLife(), sword.getDamage(), 1)
            mycursor.execute(sql, val)
            mydb.commit()
            print('角色创建成功！英雄名字:', sword.getName(), '血量:', sword.getLife(), '伤害:', sword.getDamage())
            content(sword)

        elif b=='3':

            print('你选择了女贼')
            name = input('请为你的角色起一个名字:')
            thief = Thief(name, 80, random.randint(30,40),1)
            sql = "INSERT INTO sites(name,life,damage,levle) value (%s,%s,%s,%s)"
            val = (thief.getName(), thief.getLife(), thief.getDamage(), 1)
            mycursor.execute(sql, val)
            mydb.commit()
            print('角色创建成功！英雄名字:', thief.getName(), '血量:', thief.getLife(), '伤害:', thief.getDamage())
            content(thief)

    elif a=='2':
        xname = input('请输入名字：')
        sql="SELECT  life,damage,levle FROM sites WHERE name='"+xname+"'"
        mycursor.execute(sql)
        results= mycursor.fetchone()
        xlife=results[0]
        xdamage=results[1]
        xlevel=results[2]
        if xlife==120:
            role=Knife(xname,xlife,xdamage,xlevel)
            print('您的角色为：',xname,'生命值：', xlife,'伤害：',xdamage,'等级',xlevel)
            content(role)
        elif xlife==100:
            role=Sword(xname,xlife,xdamage,xlevel)
            print('您的角色为：', xname, '生命值：', xlife, '伤害：', xdamage, '等级', xlevel)
            content(role)
        elif xlife==80:
            role=Thief(xname,xlife,xdamage,xlevel)
            print('您的角色为：', xname, '生命值：', xlife, '伤害：', xdamage, '等级', xlevel)
            content(role)


    elif a=='3':
        sys.exit(0)