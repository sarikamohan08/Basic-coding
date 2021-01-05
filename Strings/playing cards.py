t=int(input())
while(t>0):
    card_table=input()
    arr=[]
    for i in range(5):
        #ele=input()
        #arr.append(ele)
        arr=list(map(input,input().split()))
    print(arr)
    t=t-1
