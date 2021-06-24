import math

def check(arr,val):
    return(all(1<=x<=val for x in arr))

def main():
    t=int(input())
    if(1<=t<=10):
        while(t!=0):
            n,m,k=map(int,input().split())
            val=1000
            if(1<=n<=1000 and 1<=m<=1000):
                if(1<=k<=1000000000):
                    arr1=[]
                    arr2=[]
                    arr3=[]
                    for i in range(k):
                        if(i*n<=k):
                            arr1.append(i*n)
                    for i in range(k):
                        if(i*m<=k):
                            arr2.append(i*m)
                    
                    for j in range(k):
                        for l in range(j):
                            if(arr1[j]==arr2[l]):
                                arr3.append(arr1[j])
                    print(arr3)
                    
                    '''if(check(arr,val)):
                        res=math.gcd(arr[0],arr[1])
                        for i in  range(2,n):
                            res=math.gcd(res,arr[i])
        
                        print(res)'''
                    t=t-1

main()
