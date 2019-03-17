salary=int(input('请输入工资'))
temp = salary - 2000
if temp <= 0:
  print("您不需要纳税")
elif 0 < temp <= 500:
  tax = temp*0.05
elif 500 < temp <= 2000:
  tax = (temp - 500)*0.1 + 25
elif 2000 < temp <= 5000:
  tax = (temp - 2000)*0.15 + 175
elif 5000 < temp <= 20000:
  tax = (temp - 5000)*0.2 + 625
elif 20000 < temp <= 40000:
  tax = (temp - 20000)*0.25 + 3625
elif 40000 < temp <= 60000:
  tax = (temp - 40000)*0.3 + 8625
elif 60000 < temp <= 80000:
  tax = (temp - 60000) * 0.35 + 14625
elif 80000 < temp <= 100000:
  tax = (temp - 80000) * 0.4 + 21625
elif temp > 100000:
  tax = (temp - 100000)*0.45 +29625

print("您的月薪为",salary,"元,应纳税额",tax,"元")

