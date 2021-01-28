n,k=map(int,input().split())
s=0
l=[]
for i in range(1,n+1):
    l.append(i*5)


h=240-k
count=0
for i in range(len(l)):
    if(l[i]<=h):
        count+=1
print(count)
