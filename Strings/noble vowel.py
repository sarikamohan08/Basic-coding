##t=int(input())
##while(t>0):
##    n=input()
##    for i in n:
##        if(n[i]=='a'or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u'  or n[i]=='A'or n[i]=='E' or n[i]=='I' or n[i]=='O' or n[i]=='U'):
##           print("yes")
##           break;
##        else:
##            if(n[i+1]!='a'or n[i+1]!='e' or n[i+1]!='i' or n[i+1]!='o' or n[i+1]!='u' or n[i+1]!='A'or n[i+1]!='E' or n[i+1]!='I' or n[i+1]!='O' or n[i+1]!='U'):
##                print("no")
##                break;     
##            
##    t=t-1

t=int(input())
while(t>0):
    n=input()
    for i in n:
        if(i=='a'or i=='e' or i=='i' or i=='o' or i=='u'  or i=='A'or i=='E' or i=='I' or i=='O' or i=='U'):
           print("yes")
           break;
        else:
            if(i+1!='a'or i+1!='e' or i+1!='i' or i+1!='o' or i+1!='u' or i+1!='A'or i+1!='E' or i+1!='I' or i+1!='O' or i+1!='U'):
                print("no")
                break;     
            
    t=t-1
