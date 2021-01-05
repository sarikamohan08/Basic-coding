def checkYear(year):
 
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));
 
def main():
    t=int(input())
    while(t>0):
        n=int(input())
        if(checkYear(n)):
            print("Yes")
        else:
            print("No")
        t=t-1
main()
