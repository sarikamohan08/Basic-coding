def power(a,b,m):
    res=1
    while(b):
        if(b&1):
            res=((res%m)*(a%m))%m

        a=((a%m)*(a%m))%m
        b=b>>1
    return(res+m%m)%m


def main():
    t=int(input())
    while(t!=0):
        a,b,m=map(int,input().split())
        print(power(a,b,m))
        t=t-1
main()
