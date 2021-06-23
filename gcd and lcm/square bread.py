import math
import sys 
  
# Using sys.getrecursionlimit() method 
# to find the current recursion limit
limit = sys.getrecursionlimit()
'''def gcd(a,b):
    if(a==b):
        return a
    if(a==0):
        return b
    if(b==0):
        return a
    if(a>b):
        (gcd(a-b,b))
    else:
      (gcd(a,a-b))'''
    
def square(a,b):
    if(a==b):
        return 1
    else:
        m=math.gcd(a,b)
        res=(a*b)//(m**2)
        return(res)

t=int(input())
while(t>0):
    a,b=map(int,input().split())
    print(square(a,b))
    t=t-1
