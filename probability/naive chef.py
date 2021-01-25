def main():
    t=int(input())
    while(t!=0):
        n,a,b=map(int,input().split())
        arr=list(map(int,input().split()))
        countA=0
        countB=0
        for ele in arr:
            if(ele==a):
                countA+=1
            if(ele==b):
                countB+=1

        ans=(countA/n)+(countB/n)
        print(ans)
        t=t-1
main()
