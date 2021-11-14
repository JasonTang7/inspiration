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
    for j in range(n):
        a = sys.stdin.readline().split()
        time1.append([int(a[0]) , int(a[1])])
    time1.sort(key= lambda x:x[0])
    # for m in range(len(time1)):
    #     time4.append(int(time1[m]))
    for k in range(len(time1)):
        if time1[k][0] >= start:
            time2.append(time1[k])
            start = time1[k][1]
    for l in range(len(time2)):
        time3 = time3 + (time2[l][1]-time2[l][0])
    max_time.append(time3)

print(max(max_time))

