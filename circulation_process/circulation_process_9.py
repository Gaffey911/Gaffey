for x in range(1,36):
    for y in range(1,36):
        z=36-x-y
        if(x*4+y*3+z/2==36) and z%2==0:
            print("男人",x,"女人",y,"小孩",z)