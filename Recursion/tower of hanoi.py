def hanoi(n,s,d,h):
    if(n==1):
        print("move from source to destination",s,"to",d)
        return
    hanoi(n-1,s,h,d)
    print("move from source to destination",s,"to",d)
    hanoi(n-1,h,d,s)
def main():
    n=int(input())
    a=1
    b=2
    c=3
    print(hanoi(n,a,c,b))
main()
