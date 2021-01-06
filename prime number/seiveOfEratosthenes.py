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
    n=int(input())
    seive=sieveOfEro(n)
    for i in range(2,n+1):
        if(seive[i] is True):
            print(i,end=' ')
    print()
    t=t-1
seive(t)
