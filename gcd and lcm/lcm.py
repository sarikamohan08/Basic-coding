import math

def main():
    t=int(input())
    while(t!=0):
        a,b=map(int,input().split())
        lcm=a*b//math.gcd(a,b)
        print(lcm)
        t=t-1

main()
