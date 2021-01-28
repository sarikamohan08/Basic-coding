def peakElement(arr,n,low,high):
  
    mid=low+(high-low)//2
    if((mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid])):
        return id
    elif(mid>0 and arr[mid-1]>arr[mid]):
        return peakElement(arr,n,low,mid-1)
    else:
        return peakElement(arr,n,mid+1,high)

def main():
    t=int(input())
    while(t>0):
        n=int(input())
        arr=list(map(int,input().split()))
        res=(peakElement(arr,n,0,n-1))
        print(arr[res])
        t=t-1
if __name__=='__main__':
    main()
