def check(arr,n):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if(arr[i]-1==0 and arr[j]-1==0):
                #return True
                continue
            else:
              return False
n=int(input())
arr=list(map(int,input().split()))
r=check(arr,n)
if(r==True):
    print("YES")
else:
    print("NO")
  
