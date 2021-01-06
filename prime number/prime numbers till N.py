import math

def prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
           return False
    return True
t=int(input())
while(t>0):
    n=int(input())
    for i in range(2,n+1):
        if(prime(i)):
            print(i,end=' ')
    print()
        
    t=t-1

