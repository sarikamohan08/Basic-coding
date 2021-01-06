def pattern(n):
    if(n<=0):
        print(n,end = ' ')
        return
    print(n,end = ' ')
    pattern(n-5)
    print(n,end = ' ')
    return
t=int(input())
for i in range(t):
  n=int(input())
  pattern(n)
  print()
