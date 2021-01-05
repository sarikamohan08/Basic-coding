def rightrotate(arr,n):
    temp=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
    
def leftrotate(arr,n):
    temp=arr[0]
    for i in range(1,n,1):
        arr[i-1]=arr[i]
    arr[n-1]=temp
    
def printarr(arr,n):
    for i in range(n):
        print(arr[i],end=' ')
    print()
def main():
    t=int(input())
    while(t>0):
        n,k=map(int,input().split())
        arr=list(map(int,input().split()))
        for i in range(k):
            rightrotate(arr,n)
            #leftrotate(arr,n)
        printarr(arr,n)
        t=t-1

main()
