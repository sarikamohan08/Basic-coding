def gcd(a,b):
    if(a==0):
        return b
    if(b==0):
        return a
    if(a==b):
        return a
    if(a>b):
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)

t=int(input())
while(t>0):
    a,b=map(int,input().split())
    print(gcd(a,b))
    t=t-1
