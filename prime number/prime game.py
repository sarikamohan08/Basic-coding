import math
def sieveOfEro(n):
    seive=[True]*(n+1)
    seive[1]=False
    for i in range(2,int(math.sqrt(n))+1):
        if(seive[i] is True):
            for j in range(i*i,n+1,i):
                seive[j]=False
    return seive
t=int(input())
while(t>0):
    l=[]
    n=int(input())
    seive=sieveOfEro(1000001)
    for i in range(2,1000001):
        if(seive[i] is True):
            l.append(i)
    
    for j in range(1,len(l)):
        if(j==n):
            print(l[j-1])
    t=t-1         
