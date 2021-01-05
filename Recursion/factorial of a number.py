def fact(n):
    if(n==0 or n==1):
        return 1
    return(n*fact(n-1))

def main():
    n=int(input("enter no:"))
    print(fact(n))
main()
