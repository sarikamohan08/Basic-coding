
t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    winning=n//2
    dic={}
    freq=[0]*40
    for i in range(n):
        freq[arr[i]]+=1

    for i in range(40):
        if(freq[i]>0):
            dic[i].append(freq[i])
        print(dic)

    flag=0
    for i in range(40):
        if(freq[i]>1):
            flag=1
            break
    
    t=t-1
