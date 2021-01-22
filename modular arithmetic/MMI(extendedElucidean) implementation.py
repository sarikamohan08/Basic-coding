def extendEuclid(a,b):
    if(b==0):
        return 1,0,a
    x1,y1,gcd=extendEuclid(b,a%b)
    x=y1
    y=x1-y1*(a//b)
    return x,y,gcd

def main():
    t=int(input())
    while(t!=0):
        a,b,m=map(int,input().split())
        x,y,gcd=(extendEuclid(b,m))
        if(gcd!=1):
            print("MMI DOES NOT EXISTS")
        else:
            print((x%m+m)%m)
            print(((a%m)*(x%m))%m)
        t=t-1

main()
