t =int(input())
while(t>0):
    n =int(input())
    arr =list(map(int,input().split()))
    maxi=-1
    mini=1000001
    for i in range(n):
        if(arr[i]<mini):
            mini=arr[i]
        if(arr[i]>maxi):
            maxi=arr[i]
    print(mini,maxi)
    t=t-1
