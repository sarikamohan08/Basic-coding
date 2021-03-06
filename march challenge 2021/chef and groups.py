t=int(input())
while(t>0):
    s=input()
    count=0
    for i in range(len(s)):
        if((s[i]=='1')):
           count+=1
    c1=count
    for i in range(len(s)-1):
        if(s[i]=='1' and s[i+1]=='1'):
            c1=c1-1
    print(c1)
    t=t-1
