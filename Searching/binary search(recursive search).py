def RecbinarSearch(arr,low,high,target):
    if(low>high):
        return -1
    mid=low+(high-low)//2
    if(arr[mid]==target):
        return mid
    
    if(arr[mid]>target):
        RecbinarSearch(arr,mid+1,high,target)
    else:
        RecbinarSearch(arr,low,mid-1,target)
  

t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    target=int(input())
    res=RecbinarSearch(arr,0,n-1,target)
    if(res==-1):
        print("element not found")
    else:
        print("element found at index:",res)
    
    t=t-1
