def lower(mat1,n,m):
    for i in range(n):
        for j in range(m):
            if(i<j):
                print("0",end=' ')
            else:
                print(mat1[i][j],end=' ')
        print()
            


def upper(mat1,n,m):
    for i in range(n):
        for j in range(m):
            if(i>j):
                print("0",end=' ')
            else:
                print(mat1[i][j],end=' ')
        print()
            
n,m=map(int,input().split())
mat1=[]


for i in range(n):
    mat1.append(list(map(int,input().split())))


lower(mat1,n,m)
upper(mat1,n,m)

