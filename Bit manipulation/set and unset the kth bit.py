#set the kth bit
n,k=map(int,input().split())
n=n|(1<<k)
print(n)
print(bin(107))
print(bin(111))
print(int("1101111",2))

#unset the kth bit
n1,k1=map(int,input().split())
n1=n1&~(1<<k1)
print(n1)
