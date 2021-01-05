def check1(liststr1):
    s=0
    if(liststr1=='a' or liststr1=='e' or liststr1=='i' or liststr1=='o' or liststr1=='u' or liststr1=='A' or liststr1=='E' or liststr1=='I' or liststr1=='U'):
        s=1
        return s
    
def check(liststr1):
    len_list1=len(liststr1) 
    r=0
    for i in range(len_list1): 
          if(liststr1[i]=='a'or liststr1[i]=='e' or liststr1[i]=='i' or liststr1[i]=='o' or liststr1[i]=='u'  or liststr1[i]=='A'or liststr1[i]=='E' or liststr1[i]=='I' or liststr1[i]=='O' or liststr1[i]=='U'):
                if(liststr1[i+1]!='a'or liststr1[i+1]!='e' or liststr1[i+1]!='i' or liststr1[i+1]!='o' or liststr1[i+1]!='u' or liststr1[i+1]!='A'or liststr1[i+1]!='E' or liststr1[i+1]!='I' or liststr1[i+1]!='O' or liststr1[i+1]!='U'):          
                      r=1
                    #return True
        
    return r  
       

    
t=int(input())
while(t>0):
    str1=input() 
    liststr1=list(str1)
    if((len(liststr1))==1):
        s=check1(liststr1)
        if(s==1):
            print("YES")
        else:
            print("NO")
    else:
        r=check(liststr1)
        if(r==1):
            print("YES")
        else:
            print("NO")

    t=t-1
