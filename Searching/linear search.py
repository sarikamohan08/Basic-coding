t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    s=int(input())
    flag=0
    for i in range(len(arr)):
        if(arr[i]==s):
            flag=1
            print("element not found at index:",i)
            break
    if(flag==0):
        print("element not found")
    t=t-1
