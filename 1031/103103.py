from _typeshed import Self
import sys
nm = input().split(" ")
n = int(nm[0])
m = int(nm[1])
ans =[]
values=[]
line = sys.stdin.readline().strip()
targetlist = list(line.split())
target= targetlist[0]
for i in range(n):
    line = sys.stdin.readline().strip()
    values = list(line.split())
    for j in range(len(values)):
        if target == values[j]:
            ans.append([i,j])
print(ans)
print("NO")