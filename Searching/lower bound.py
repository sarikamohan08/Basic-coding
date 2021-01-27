def lowerBound(arr,n,target):
    low=0
    high=n
    while(low<high):
        mid=low+(high-low)//2
        
        if(arr[mid]>=target):
            high=mid
        else:
            low=mid+1
    return low

t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    q=int(input())
    while(q>0):
        ele=int(input())
        print(lowerBound(arr,n,ele))
        q=q-1
    
    t=t-1
