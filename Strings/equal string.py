t=int(input())
while(t>0):
    st1=input()
    st2=input()
    l=0
    for i in range(len(st1)):
        ll=st2[0:i]
        lr=st2[i:]
        left=lr+ll
    
        right=st2[len(st2)-i:]+st2[0:len(st2)-i]
        
        if(left==st1 or right==st1):
            l=l+1
    print(l)
    t=t-1
