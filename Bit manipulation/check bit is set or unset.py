n,k=map(int,input().split())
n=n^(1<<k)
print(n)
print(bin(107))
print(bin(123))

if(n &(1<<k)!=0):
    print("kth bit is set")
else:
    print("kth bit is unset")
