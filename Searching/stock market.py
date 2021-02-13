t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    sum1=0
    for i in range(n-1):
        if(arr[i]<arr[i+1]):
            s=arr[i+1]-arr[i]
            sum1+=s
    print(sum1)
    t=t-1
            
