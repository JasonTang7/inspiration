import sys 

T = int(input())
n = int(input())
time1=[]
time2=[]
time3= 0
time4=[]
max_time=[]
start = 8


for i in range(T):
    if n ==0:
        break
    for j in range(n):
        
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        if not values:
            break
        time1.append(values)        
    if not time1:
        continue
    time1.sort(key= lambda x:x[0])
    for k in range(len(time1)):
        if time1[k][0] >= start:
            time2.append(time1[k])
            start = time1[k][1]
    for l in range(len(time2)):
        time3 = time3 + (time2[l][1]-time2[l][0])
    max_time.append(time3)

if max_time:
    print(max(max_time))

else:
    print(0)    

