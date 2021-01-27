def upperBound(arr,n,target):
    low=0
    high=n
    while(low<high):
        mid=(high+low)//2
        if(target>=arr[mid]):
            low=mid+1
        else:
            
            high=mid
    return high

t=int(input())
while(t>0):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    res=(upperBound(arr,n,q))
    if(res==0):
        print("-1")
    else:
        print(res-1)
    t=t-1
