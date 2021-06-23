import math

def check(arr,val):
    return(all(1<=x<=val for x in arr))

def main():
    t=int(input())
    if(1<=t<=5):
        while(t!=0):
            n=int(input())
            val=10000001
            if(1<=n<=10000001):
                arr=list(map(int,input().split()))
                if(check(arr,val)):
                    res=math.gcd(arr[0],arr[1])
                    for i in  range(2,n):
                        res=math.gcd(res,arr[i])
        
                    print(res)
                    t=t-1

main()
