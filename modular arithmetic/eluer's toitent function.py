import math

def phi(n):
    res=n
    i=2
    while(i<=math.sqrt(n)):
        if(n%i==0):
            while(n%i==0):
                n=n//i
            res=res-res//i
        i+=1
        
    if(n>1):
        res=res-res//n
    return res

def main():
    t=int(input())
    while(t!=0):
        n=int(input())
        print(phi(n))
        t=t-1
main()
