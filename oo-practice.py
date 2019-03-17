class Role(object):
    def __init__(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def attack(self):
        return 0

class Magicer(Role):
    def __init__(self,name,level):
        super(Magicer,self).__init__(name)
        self.__level=level
    def getLevel(self):
        return self.__level
    def attack(self):
        return self.getLevel()*5
class Soldier(Role):
    def __init__(self,name,harm):
        super(Soldier,self).__init__(name)
        self.__harm=harm
    def getHarm(self):
        return self.__harm
    def attack(self):
        return self.getHarm()
class Team():
    l=[]*6
    r=Role('')
    def addMember(self,r):
        self.l.append(r)
        return self.l
    def attackSum(self):
        sum=0
        for i in self.l :
            sum=sum+i.attack()
        return sum
a=Magicer('a',5)
b=Soldier('b',50)
print(a.attack())
print(b.attack())
t=Team()
t.addMember(a)
t.addMember(b)
print(t.attackSum())




