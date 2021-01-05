def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
def main():
    t=int(input())
    while(t>0):
        a,b=list(map(int,input().split()))
        GCD=gcd(a,b)
        print(GCD)
        t=t-1
main()
