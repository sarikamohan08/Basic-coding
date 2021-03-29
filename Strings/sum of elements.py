t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    sum1=0
    for i in range(len(arr)):
        sum1+=arr[i]
    print(sum1)
