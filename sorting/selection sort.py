def SelectionSort(arr,n):
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if(arr[min_index]>arr[j]):
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
def main():
    t=int(input())
    while(t>0):
        n=int(input())
        arr=list(map(int,input().split()))
        SelectionSort(arr,n)
        for i in range(n):
            print(arr[i],end=' ')
        print()
        t=t-1

if __name__=='__main__':
    main()
