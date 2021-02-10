from sys import setrecursionlimit
setrecursionlimit(100000000)

def merge(arr,l,mid,r):
    n=mid-l+1
    m=r-mid
    arr1=[0]*n
    arr2=[0]*m
    for i in range(n):
        arr1[i]=arr[l+i]
    for i in range(m):
        arr2[i]=arr[mid+1+i]
        
    inv_count=0
    i=0
    j=0
    k=l
    while(i<n and j<m):
        if(arr1[i]<arr2[j]):
            arr[k]=arr1[i]
            k+=1
            i+=1
        else:
            arr[k]=arr2[j]
            inv_count+=(n-i)
            k+=1
            j+=1
    while(i<n):
        arr[k]=arr1[i]
        k+=1
        i+=1
    while(j<m):
        arr[k]=arr2[j]
        k+=1
        j+=1
    return inv_count

def mergeSort(arr,l,r):
    inv_count=0
    if(l<r):
        mid=l+(r-l)//2
        inv_count+=mergeSort(arr,l,mid)
        inv_count+=mergeSort(arr,mid+1,r)
        inv_count+=merge(arr,l,mid,r)
    return inv_count
        
def main():
    t=int(input())
    while(t>0):
        n=int(input())
        arr=list(map(int,input().split()))
        print(mergeSort(arr,0,n-1))
        
        t=t-1
main()
