def binarSearch(arr,n,target):
    low=0
    high=n-1
    while(low<=high):
        mid=low+(high-low)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            low=mid+1
        else:
            high=mid+1
    return -1

t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    target=int(input())
    res=binarSearch(arr,n,target)
    if(res==-1):
        print("element not found")
    else:
        print("element found at index:",res)
    
    t=t-1
