t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    res=arr[0]
    for i in range(1,n):
        res=res^arr[i]
    print(res)
