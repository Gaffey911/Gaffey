for x in range(1,100):
    for y in range(1,100):
        z=100-x-y
        if(3*x+2*y+z/3==100) and z%3==0:
            print("公鸡",x,"母鸡",y,"小鸡",z)