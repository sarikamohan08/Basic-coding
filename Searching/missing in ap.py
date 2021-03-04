t=int(input())
while(t>0):
    l=[]
    n=int(input())
    arr=list(map(int,input().split()))
    ap=arr[1]-arr[0]
    for i in range(n-1):
        if(arr[i+1]-arr[i]==ap):
            continue
        s=(arr[i+1]-ap)
        print(s)
    t=t-1
