import math
def sieveOfEro(n):
    seive=[True]*(n+1)
    seive[1]=False
    for i in range(2,int(math.sqrt(n))+1):
        if(seive[i] is True):
            for j in range(i*i,n+1,i):
                seive[j]=False
    return seive
t,k = [int(x) for x in input().split()]
while(t>0):
    n1=int(input())
    arr= [int(x) for x in str(n1)]
    arr1=arr[0]
    arr2=arr[-1]
    s=arr1+arr2
    seive=sieveOfEro(100000)
    l=[]
    for i in range(2,100000):
        if(seive[i] is True):
            l.append(i)
    
    if(arr1  in l and arr2  in l and s>k):
        print("Yes")
    else:
        print("no")
    t=t-1         

