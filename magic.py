'''
1.被双下划线包围起来的方法叫魔法方法
2.__init__
3.__del__
4.self other 代表参与计算的两个对象
'''
#5

class C:
    def __init__(self,*args):
        if args==0:
            print('没有传入')
        else:
            a=len(args)
            print('传入了',a,'个参数')
            print('分别是')
            for each in args:
                print(each,end=' ')
            print()
c=C('a',1,2,3,4,5,6,7)

#6

class Word(str):
    def __new__(cls,word):
        if ' ' in word:
            word=word[:word.index(' ')]
        return word
    def __gt__(self, other):
        return len(self)>len(other)
    def __lt__(self, other):
        return len(self)<len(other)
    def __le__(self, other):
        return len(self)<=len(other)
    def __ge__(self, other):
        return len(self)>=len(other)
w1=Word('hello')
w2=Word('hello1 Word')
print('w1>w2',w1>w2)
print('w1<w2',w1<w2)

#7
class NStr(str):
    def __sub__(self, other):
        return self.replace(other,' ')
a=NStr('hello world')
b=NStr('world')
print(a-b)