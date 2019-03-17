def delta(a,b,c):
      if b**2-4*a*c>=0:
            return True
      else:
            return False
def fangcheng(a,b,c):
      if delta(a,b,c):
            x1=(-b+(b**2-4*a*c)**0.5)/2*a
            x2=(-b-(b**2-4*a*c)**0.5)/2*a
            print(x1,x2)
      else:
            print('方程无解')
fangcheng(1,1,1)