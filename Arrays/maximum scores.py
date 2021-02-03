
def score(arr):
    d=[]
    x=0
    y=0
    for i in range(len(arr)):
        if(arr[i]=='0'):
            x+=1
        for j in range(i+1,len(arr)):
            if(arr[j]=='1'):
                y+=1  
        
    f=x+y
    d.append(f)
        
    return(max(d))
arr=input()
print(score(arr))

