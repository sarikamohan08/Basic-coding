t=int(input())
while(t>0):
    org=input()
    fake=input()
    ll=fake[0:2]
    lr=fake[2:]
    left=lr+ll
    
    right=fake[len(fake)-2:]+fake[0:len(fake)-2]
    if(left==org or right==org):
        print("YES")
    else:
        print("NO")
    
    t=t-1
