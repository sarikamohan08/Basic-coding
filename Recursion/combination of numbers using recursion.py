def combo(arr,output,i,index,n,k):
    #index -index for output list we put element here
    if(k==0):
        for j in range(len(output)):
            print(output[j],end='')
        print()
        return
    for j in range(i,n):
        output[index]=arr[j]
        combo(arr,output,j+1,index+1,n,k-1)
        
def main():
  t=int(input())
  while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    output=[0]*k
    combo(arr,output,0,0,n,k)
    t=t-1
main()
