n=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(n):
    for j in range(n):
        if(i!=j):
            if((arr[j]<=0.5*arr[i]+7) or (arr[j]>100 and arr[i]<100)or (arr[j]>arr[i])):
                  continue
            else:
                count+=1
print(count)
