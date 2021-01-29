n,k=map(int,input().split())
s=0
h=240-k
count=0
for i in range(n):
    s+=(i+1)*5
    if(s<h):
      count+=1
    else:
      break
print(count)
