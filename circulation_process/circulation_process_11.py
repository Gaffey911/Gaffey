n=int(input("输入一个整数"))
for i in range(1, n+1):
     for j in range(0, n-i):
         print (" ",end=" ")
     for k in range(0, 2*i -1):
             print("*",end=" ")
     print("\n")
