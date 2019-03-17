class Employee(object):
    def __init__(self,name,birth):
        self.name=name
        self.birth=birth
    def getSalary(self,month):
        if month==self.birth:
            return 100
        else:
            return 0


class SalariedEmployee(Employee):
    def __init__(self,name,birth,salary):
        super(SalariedEmployee,self).__init__(name,birth)
        self.salary=salary
    def getSalary(self,month):
        return self.salary+Employee.getSalary(self,month)
class HourlyEmployee(Employee):
    def __init__(self,name,birth,hsalary,hwork):
        super(HourlyEmployee,self).__init__(name,birth)
        self.hsalary=hsalary
        self.hwork=hwork
    def getSalary(self,month):
        if self.hwork>160:
            return 160*self.hsalary+(self.hwork-160)*1.5*self.hsalary+Employee.getSalary(self,month)
        else:
            return self.hsalary*self.hwork+Employee.getSalary(self,month)
class SalesEmployee(Employee):
    def __init__(self,name,birth,sale,extra):
        super(SalesEmployee, self).__init__(name, birth)
        self.sale=sale
        self.extra=extra
    def getSalary(self,month):
        return self.sale*self.extra+Employee.getSalary(self,month)
class BasedPlusSalesEmployee(Employee):
    def __init__(self,name,birth,sale,extra,base):
        super(BasedPlusSalesEmployee,self).__init__(name,birth)
        self.sale=sale
        self.extra=extra
        self.base=base
    def getSalary(self,month):
        return self.base+self.sale*self.extra+Employee.getSalary(self,month)
a=SalariedEmployee('a',10,10000)
b=HourlyEmployee('b',9,20,200)
c=SalesEmployee('c',8,20000,0.3)
d=BasedPlusSalesEmployee('d',7,20000,0.3,5000)
print(a.getSalary(9))
print(b.getSalary(9))
print(c.getSalary(9))
print(d.getSalary(9))

