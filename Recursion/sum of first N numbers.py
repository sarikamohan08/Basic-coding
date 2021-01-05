from sys import setrecursionlimit
setrecursionlimit(11000)

def sum1(n):
    if(n==1):
        return 1
    
    return n+sum1(n-1)

def main():
    n=int(input())
    print(sum1(n))
main()
