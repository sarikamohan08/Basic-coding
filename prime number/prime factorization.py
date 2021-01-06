import math

t=int(input())
while(t>0):
    n=int(input())
    if(n<2):
        flag=True
    arr=[]
    for i in range(2,int(math.sqrt(n)+1)):
        while(n%i==0):
            n=n//i
            arr.append(i)
            break
        if(n>1):#threfore prime number
            arr.append(n)
        if(n==1):
            break
    for i in range(0,len(arr)):
        print(arr[i],end=' ')
    print()
    t=t-1
