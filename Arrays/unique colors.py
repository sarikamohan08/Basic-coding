def getunique(arr):
    res={}
    for ele in arr:
        if ele in res:
            res[ele]+=1
        else:
            res[ele]=1
    l=[]
    for ele in res:
        if (res[ele]==1):
            l.append(ele)
    print(len(l))
    
count=int(input())
arr=[int(ele) for ele in input().split(" ")]
getunique(arr)
   
