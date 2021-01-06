def reverse(str1):
    if len(str1) == 0:
        return str1
    else:
        return reverse(str1[1:]) + str1[0]
    
t=int(input())
while(t>0):
    n=(input())
    h=reverse(n)
    if(h==n):
        print("Yes")
    else:
        print("No")
    
    t=t-1
