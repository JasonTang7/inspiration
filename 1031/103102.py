listA=input().strip("-")
listB=input().strip("-")

listpai =['3','4','5','6','7','8','9','10','J','Q','K','A']
listleftpainums=[]
maxshunzi=[]
shunzileft=[]
shunziright=[]
ans=[]
ans1=[]
for i in range(len(listpai)):
    nums =0
    for j in range(len(listA)):
        if listpai[i] == listA[j]:
            nums = nums +1
    for k in range(len(listB)):
        if listpai[i] == listB[k]:
            nums = nums +1
    leftnums = 4 -nums
    listleftpainums.append(leftnums)
shunzinums = 0
l=0
for i in range(len(listleftpainums)):
    if listleftpainums[i] != 0:
        shunzinums = shunzinums +1
    elif i == len(listleftpainums)-1 or listleftpainums[i] == 0 :
        maxshunzi.append(shunzinums)
        shunzileft.append(l)
        shunziright.append(i)
        if len(maxshunzi)>1 and maxshunzi[1] < maxshunzi[0]:
            del maxshunzi[1]
            del shunzileft[1]
            del shunziright[1]
        elif len(maxshunzi)>1:
            del maxshunzi[0]
            del shunzileft[0]
            del shunziright[0]
        l =i+1
        shunzinums = 0
if len(shunziright)>0 and shunziright[0] - shunzileft[0] <5:
    print("NO-CHAIN")
elif shunzileft:
    ans.append(listpai[shunzileft[0]:shunziright[0]])
    for i in range(shunziright[0]-shunzileft[0]):
        ans1.append(ans[0][i])
        if i != shunziright[0]-shunzileft[0]-1:
            ans1.append("-")
    for i in range(len(ans1)):
        print(ans1[i],end="")

    

