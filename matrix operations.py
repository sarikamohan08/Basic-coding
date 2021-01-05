n,m=map(int,input().split())
mat1=[]
mat2=[]
mat3=[]
mat4=[]
for i in range(n):
    mat1.append(list(map(int,input().split())))

for i in range(n):
    mat2.append(list(map(int,input().split())))


for i in range(n):
    mat3.append([0]*m)
l1=[]
print("AdditionMatrix=")
for i in range(n):
    for j in range(m):
        mat3[i][j]=mat1[i][j]+mat2[i][j]
        l1.append(mat3[i][j])
       
for i in range(n):
    for j in range(m):
        print(mat3[i][j],end=' ')
    print()

print("MultiplicationMatrix=")
for i in range(n):
    mat4.append([0]*m)
    
for i in range(n):
    for j in range(m):
        for k in range(m):
            mat4[i][j]=mat4[i][j]+(mat1[i][k]*mat2[k][j])

for i in range(n):
    for j in range(m):
        print(mat4[i][j],end=' ')
    print()

