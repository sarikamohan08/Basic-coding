n,h,x=map(int,input().split())
arr=list(map(int,input().split()))
flag=0
for i in range(len(arr)):
    if(arr[i]+x>=h):
        flag=1

if(flag==1):
    print("YES")
else:
    print("NO")
    
