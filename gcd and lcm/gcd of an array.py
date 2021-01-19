import math

def main():
    t=int(input())
    while(t!=0):
        n=int(input())
        arr=list(map(int,input().split()))
        res=math.gcd(arr[0],arr[1])
        for i in  range(2,n):
            res=math.gcd(res,arr[i])
        
        print(res)
        t=t-1

main()
