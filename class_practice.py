'''
1.类是生产对象的模板
2.具体
3.私有属性
4.函数定义在类的外部，方法定义在类的内部
5.__init__
6.self:接收实例化过程中传入的所有数据
'''
#T7
class Person:
    name='zqy'
    age=18
    def print(self):
        print(Person.name)
me=Person()
me.print()
#T8
class Worker:

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def work(self,time):
        self.time=time

#T9
class Tickets:
    def __init__(self,time,adult,child):
        self.time=time
        self.adult=int(adult)
        self.child=int(child)
    def price(self):
        if self.time=="周末":
            aprice=120
            cprice=60
        if self.time=="工作日":
            aprice=100
            cprice=50
        price=aprice*self.adult+cprice*self.child
        print(self.adult,"个成年人",self.child,"个小孩一共",price,"元")
time=input("去公园的时间是周末还是工作日？")
adult=int(input('输入成人人数'))
child=int(input("输入儿童人数"))
t=Tickets(time,adult,child)
t.price()
#T10
class Address:
    def __init__(self,addres,zipCode):
        self.address=addres
        self.zipCode=zipCode
#T11
class Worker:
    def __init__(self,name,age,salary,address,zipCode):
        self.name=name
        self.age=age
        self.salary=salary
        Address.address=address
        Address.zipCode=zipCode
    def print(self):
        print(self.name,self.age,self.salary,Address.address,Address.zipCode)
w=Worker('zhang3',25,2500,'北京市海淀区清华园1号',100084)
w.print()