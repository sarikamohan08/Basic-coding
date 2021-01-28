def sun(arr,n):
    count=1
    high=arr[0]
    for i in range(1,n):
       if(arr[i]>high):
           high=arr[i]
           count+=1
           
    return count   
                
t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    print(sun(arr,n))
    t=t-1
