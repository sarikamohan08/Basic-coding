def check(arr,n):
  r=0
  for i in range(len(arr)+1):
        arr[i]=arr[i]-1
        arr[i+1]=arr[i+1]-1

  ele=arr[0]
  chk=0
  for i in arr: 
        if ele != i: 
            chk = 1
            break;
            
            
        if (chk == 0):
            print("YES") 
            
        else:
            print("NO")
   
n=int(input())
arr=list(map(int,input().split()))
r=check(arr,n)
##if(r==1):
##  print("YES")
##else:
##    print("NO")
