t=int(input())
while(t>0):
    arr=(input())
    freq=[0]*26
    for i in range(len(arr)):
        freq[ord(arr[i])-97]+=1
    flag=0
    l=[]
    for i in range(0,26):
        
        if(freq[i]>0):
            a=("{}".format(chr(i+97)))
            l.append(a)
            flag=1
            freq[i]=freq[i]-1   

    if(flag==0):
        print("-1")

    else:
        s=' '
        for n in l:
            s=n+s
        print(s)
            
    t=t-1
