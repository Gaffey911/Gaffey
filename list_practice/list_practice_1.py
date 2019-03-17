#第三题
list1=['H','L','L','O']
list1.insert(1,'E')
for i in list1:
    print(i,end='')
print()
#第四、五题
list2=[1,3,2,9,7,8,]
print(list2[2:5])
print(list2[-3:-1])
#第六题
list3=[1,2,3,4]
a=list3.pop()
list3.insert(0,a)
print(list3)
#第七题
list4=['hello','world','python',1,2,3,['zhang3','li4']]
list4[-1][0]='wang5'
print(list4)
#第八题
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
count=0
while len(list)>1:
    count+=1
    list.append(list.pop(0))
    if count==7:
        count=0
        list.pop()
for i in list:
    print('猴子大王是第',i,'只猴子')