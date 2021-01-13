def gcd(a,b):
    if(b==0):
        return a

    return gcd(b,a%b)

def main():
    t=int(input())
    while(t!=0):
        a,b=map(int,input().split())
        print(gcd(a,b))
        t=t-1
main()
