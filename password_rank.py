'''密码检测函数
输入一段代码，返回密码级别及提高密码级别方法
低级密码，长度大于0且密码由纯数字或字母组成
中级密码，长度不小于8且密码由数字，字母，特殊字符中的两种或两种以上组成
高级密码，长度大于16且密码由数字 字母，特殊字符三种组成。
'''

def rankpw():
    pw=input()
    a = 0
    b = 0
    c = 0
    for i in pw:
        if i.isalpha() == True:
            a += 1
        elif i.isdecimal() == True:
            b += 1
        else:
            c += 1
    if len(pw)>0 and (a>0 and b==0 and c==0):
        print("密码等级低，请勿使用纯字母")
        reinput()
    elif len(pw)>0 and (a==0 and b>0 and c==0):
        print("密码等级低，请勿使用纯数字")
        reinput()
    elif len(pw)<8 and (a>0 and b>0 and c>0):
        print("密码等级低，建议增加长度")
        reinput()
    elif len(pw)>=8 and (a>0 and b>0 and c==0):
        print("密码强度中等，建议加入特殊字符")
        reinput()
    elif len(pw)>=8 and (a>0 and c>0 and b==0):
        print("密码强度中等，建议加入字母")
        reinput()
    elif len(pw)>=8 and (a==0 and b>0 and c>0):
        print("密码强度中等，建议加入数字")
        reinput()
    elif len(pw)>=8 and len(pw)<16 and (a>0 and b>0 and c>0):
        print("密码强度中等，建议增加长度")
        reinput()
    elif len(pw)>16 and (a>0 and b>0 and c>0):
        print("密码强度高级")
def reinput():
    print("请重新输入密码")
    rankpw()


print("请输入密码(字母数字或特殊字符)：")
rankpw()


