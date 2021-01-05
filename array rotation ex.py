def reverserightalgo(arr,i,j):
    while(i<j):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1


def printarr(arr,n):
    
    for i in range(n):
      print(arr[i],end=' ')
    
def main():
    t=int(input())
    while(t>0):
        n,k=map(int,input().split())
        k=k%n
        arr=list(map(int,input().split()))
        reverserightalgo(arr,n-k,n-1)
        reverserightalgo(arr,0,n-k-1)
        reverserightalgo(arr,0,n-1)
        printarr(arr,n)
        
        t=t-1

main()
