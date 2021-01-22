import math

def fastExponent(a,b,m):
    res=1
    while(b>0):
        if(b&1):
            res=((res%m)*(a%m))%m
        a=((a%m)*(a%m))%m
        b=b>>1
    return (res%m+m)%m

def main():
    t=int(input())
    while(t!=0):
        a,m=map(int,input().split())
        if(math.gcd(a,m)!=1):
            print("MMI does not exist")
        else:
            print(fastExponent(a,m-2,m))
        t=t-1
main()
