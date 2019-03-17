weight=int(input('请输入重量（单位kg）'))
if weight<=20:
    print('收费5元')
elif 20<weight<=100:
    money=(weight-20)*0.2+5
    print('收费',money,'元')
elif weight>100:
    money=(weight-100)*0.15+(weight-20)*0.2+5+5
    print('收费',money,'元')