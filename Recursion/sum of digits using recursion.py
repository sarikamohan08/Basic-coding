from sys import setrecursionlimit
setrecursionlimit(11000)

def sum1(n):
    tot=0
    if(n==0):
        return 0
    return (n%10 +sum1(int(n/10)))

def main():
  t=int(input())
  while(t>0):
    n=int(input())
    h=(sum1(n))
    print(h)
    t=t-1
main()
