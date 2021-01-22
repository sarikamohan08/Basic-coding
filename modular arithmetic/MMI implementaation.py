import math

def main():
    t=int(input())
    while(t!=0):
        a,m=map(int,input().split())
        if(math.gcd(a,m)!=1):
            print("MMI does not exist")
        else:
            for x in range(1,m):
                if((a%m)*(x%m)%m==1):
                    print(x)
                    break
        t=t-1

if __name__=='__main__':
    main()
