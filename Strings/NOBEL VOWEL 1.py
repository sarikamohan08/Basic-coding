
def vowel(liststr1):
    if(liststr1=='a' or liststr1=='e' or liststr1=='i' or liststr1=='o' or liststr1=='u' or liststr1=='A' or liststr1=='E' or liststr1=='I' or liststr1=='U'):
       pass
t=int(input())
while(t>0):
    str1=input() 
    liststr1=list(str1)
    flag=True
    bool(flag)
    for i in range(len(liststr1)):
        if(not vowel(liststr1[i])):
            if(not vowel(liststr1[i+1] and (liststr1[i+1]!='n'))):
                flag=False
                break
    if(flag=="True"):
        print("YES")
    else:
        print("NO")
    t=t-1
