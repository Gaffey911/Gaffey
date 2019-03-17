age=int(input("请输入年龄"))
if age>0 and age<6:
    print("儿童")
elif 6<=age<=13:
    print("少儿")
elif 14 <= age <= 17:
    print("青少年")
elif 18<= age <=35:
    print("青年")
elif 36<= age <=50:
    print("中年")
elif 50<age:
    print("中老年")