t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    flag=0
    for i in range(len(arr)):
        if(arr[i]==1):
            flag=1
            print("hard")
            break
    if(flag==0):
        print("easy")
    t=t-1
