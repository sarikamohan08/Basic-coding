t=int(input())
while(t>0):
    n=(input())
    arr=list(n)
    ar1=len(arr)
    l=0
    s=0
    for i in range(ar1):
        if(arr[i]=='a'):
           l+=1
        else:
            s+=1
    if(l>ar1//2):
        print(ar1)
    else:
        h=2*l-1
        print(h)
    t=t-1
            
