t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(n+1):
        d=arr[i]+arr[i+1]==arr[i]/arr[i+1]
    print(d)
    t=t-1
    
