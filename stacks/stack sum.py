def maxSum(stack1,stack2,stack3,n,m,x):
    sum1=0
    sum2=0
    sum3=0
    for ele in stack1:
        sum1+=ele
    for ele in stack2:
        sum1+=ele
    for ele in stack3:
        sum1+=ele
    while(True):
        if(len(stack1)==0 or len(stack2)==0 or len(stack2)==0 ):
            return 0
        if(sum1==sum2 and sum2==sum3):
            return sum1
        if(sum1>=sum2 and sum1>=sum3):
            sum1-=stack1[-1]
            stack1.pop()

        elif(sum2>=sum2 and sum2>=sum3):
            sum2-=stack2[-1]
            stack2.pop()

        else:
            sum3-=stack3[-1]
            stack3.pop()
        
        
    
def main():
    t=int(input())
    while(t>0):
        n,m,x=map(int,input().split())
        stack1=list(map(int,input().split()))
        stack1.reverse()
        stack2=list(map(int,input().split()))
        stack2.reverse()
        stack3=list(map(int,input().split()))
        stack3.reverse()

        print(maxSum(stack1,stack2,stack3,n,m,x))
        t=t-1
main()
