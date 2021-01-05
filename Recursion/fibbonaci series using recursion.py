def fib(n):
    if(n==0 or n==1):
        return n
    x=fib(n-1)
    y=fib(n-2)
    return x+y

def main():
  t=int(input())
  while(t>0):
    n=int(input())
    print(fib(n))
    t=t-1
main()
