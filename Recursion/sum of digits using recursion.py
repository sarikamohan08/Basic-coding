from sys import setrecursionlimit
setrecursionlimit(11000)

def sum1(n):
    for i in range(len(n)):
        if(n==1):
            return 1
    
        return n+sum1(n-1)

def main():
  t=int(input())
  while(t>0):
    n=int(input())
    arr=list(n)
    print(sum1(n))
    t=t-1
main()
