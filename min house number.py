
t =int(input())
while(t>0):
    n =int(input())
    arr =list(map(int,input().split()))

    mini=1000001
    for i in range(n):
        if(arr[i]<mini):
            mini=arr[i]
    print((list(map(int,mini.split()))))
    t=t-1
