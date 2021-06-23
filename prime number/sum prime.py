import math
def sieveOfEro(n):
    seive=[True]*(n+1)
    seive[1]=False
    for i in range(2,int(math.sqrt(n))+1):
        if(seive[i] is True):
            for j in range(i*i,n+1,i):
                seive[j]=False
    return seive
    
def is_prime(n):
    if n in[3,5,7]:
        return True
    return False

t=int(input())
while(t>0):
    n=int(input())
    seive=sieveOfEro(500)
    #print(seive)
    l=[]
    for i in range(2,500):
        if(seive[i] is True):
            l.append(i)
    
    #print(l)
    sum1=0
    odd=[3,7,11]
    for i in range(len(l)):
        flag=1
        a=l[i]
        while(a!=0):
            d=a%10
            a=a//10
            if(is_prime(d)):
                flag=0
                break
        if(flag==1):
            n=n-1
            sum1=sum1+l[i]
        if(n==0):
            break
    print(sum1)
    t=t-1         


