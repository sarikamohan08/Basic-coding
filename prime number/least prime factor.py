import math
def lpf(n):
    seive=[0]*(n+1)
    for i in range(2,n+1):
        if(seive[i]==0):
            seive[i]=i
            for j in range(i*i,n+1,i):
                if(seive[j]==0):
                    seive[j]=i
    return seive
t=int(input())
while(t>0):
    n=int(input())
    seive=lpf(n)
    for i in range(2,n+1):
            print(i,"=",seive[i])
    print()
    t=t-1
seive(t)
