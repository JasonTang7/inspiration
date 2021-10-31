import sys
slist = input().split(",")
firstnum = []
answer=[]
for i in range(len(slist)):
    firstnum.append(int(slist[i][0]))
cfirstnum=firstnum[:]
cfirstnum.sort(reverse=True)
for i in range(len(cfirstnum)):
    for j in range(len(firstnum)):
        if cfirstnum[i] == firstnum[j] and slist[j] not in answer:
            answer.append(slist[j])
            break
print("".join(answer))


