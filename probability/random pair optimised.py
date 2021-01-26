def main():
    t=int(input())
    while(t!=0):
        n=int(input())
        arr=list(map(int,input().split()))
        arr.sort()
        max_val=-1
        maxEle=arr[n-1]
        total=(n*(n-1))//2
        count1=arr.count(maxEle)
        if(count1==1):
            count2=arr.count(arr[n-2])
            print(count2/total)
        else:
            val=(count1*(count1-1))/2
            print(val/total)

        
        t=t-1
main()
