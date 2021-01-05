t =int(input())
while(t>0):
    n =int(input())
    arr =list(map(int,input().split()))
    l=[]
    for i in range(n):
          if(i==0):
            if(arr[i]>arr[i+1]):
                  l.append(i)  
              
          elif(i==n or i==n-1):
            if(arr[i]>arr[i-1]):
                 l.append(i)
                    
          elif(arr[i]==arr[i+1] or arr[i]==arr[i-1]):
              pass
            
          else:
            if(arr[i-1]<arr[i]>arr[i+1]):
                 l.append(i)
                 
    if(len(l)==0):
        print(-1)
    else:
        for j in range(len(l)):    
              print(l[j],end=' ')
        print()
    t=t-1
    
