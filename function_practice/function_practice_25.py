def distance():
    x1=float(input('请输入坐标x1'))
    y1=float(input('请输入坐标y1'))
    x2=float(input('请输入坐标x2'))
    y2=float(input('请输入坐标y2'))
    dis=((x1-x2)**2+(y1-y2)**2)**0.5
    print(dis)
distance()