from sys import setrecursionlimit
setrecursionlimit(10000000)
def partition(arr,low,high):
    x=arr[high]
    i=low-1
    for j in range(low,high):
        if(arr[j]<=x):
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quicksort(arr,low,high):
    if(low<high):
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)
                  
def main():
    t=int(input())
    while(t!=0):
        n=int(input())
        arr=list(map(int,input().split()))
        quicksort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=' ')
        print()
        t=t-1
main()
