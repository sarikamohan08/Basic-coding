t=int(input())
while(t>0):
    n=int(input())
    if(n<2):
        flag=True
    for i in range(2,n-1):
        if(n%i==0):
            flag=False
            
            break;
        else:
            
            break
    if(flag):
        print("prime")
    else:
        print("not prime")
    t=t-1
