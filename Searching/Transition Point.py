def transitionPoint(arr):
    for i in range(len(arr)):
        if(arr[i]==1):
            return i
   
t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    flag=(transitionPoint(arr))
    if(flag==None):
        print("-1")
    else:
        print(flag)
    t=t-1
