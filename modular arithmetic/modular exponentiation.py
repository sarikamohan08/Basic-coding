import math

def modExp(a,b,m):
    if(a==0):
        return 0
    if(b==0):
        return 1
    if(b%2==0):
        res=modExp(a,b//2,m)
        res=(res%m *res%m)%m
    else:
        ans=a%m
        res=(ans%m * modExp(a,b-1,m)%m)%m
    return(res%m+m)%m
def main():
    t=int(input())
    while(t!=0):
        a,b,m=map(int,input().split())
        print(modExp(a,b,m))
        t=t-1

if __name__=='__main__':
    main()
