n=int(input())
for i in range(31):
    curr=1<<i
    if(curr>n):
        break
    res=curr
print(res)
