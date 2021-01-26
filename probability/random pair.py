def main():
    t=int(input())
    while(t!=0):
        n=int(input())
        arr=list(map(int,input().split()))
        max_val=-1
        for i in range(0,n):
            for j in range(i+1,n):
                temp=arr[i]+arr[j]
                if(max_val<temp):
                    max_val=temp
        count=0
        for i in range(0,n):
            for j in range(i+1,n):
                temp=arr[i]+arr[j]
                if(max_val==temp):
                    count+=1
        total=(n*(n-1))//2
        print(count/total)
        t=t-1
main()
