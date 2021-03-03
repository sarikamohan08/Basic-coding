class Stack:
    def __init__(self):
        self.arr=[]
        self.tos=-1

    def push(self,data):
        self.tos+=1
        self.arr.append(data)

    def popStack(self):
        if(self.isEmpty()):
            print("stack is empty")
            return
        self.tos=self.tos-1
        self.arr.pop()
        
    def size(self):
        return self.tos+1

    def isEmpty(self):
        return self.tos==-1

    def top(self):
        if(self.isEmpty()):
            print("stack is empty")
            return
        return self.arr[self.tos]
    
def isop(str1):
    if(str1=="*"):
        return 4
    if(str1=="/"):
        return 3
    if(str1=="-"):
        return 2
    if(str1=="+"):
        return 1
    else:
        return 0
def main():
    st=Stack()
    n=int(input())
    arr=list(input().split())
    for i in range(n):
        val=isop(arr[i])
        if(val==0):
            st.push(int(arr[i]))
        else:
            op1=st.top()
            st.popStack()
            op2=st.top()
            st.popStack()
            if(val==4):
                st.push(op2*op1)
            if(val==3):
                st.push(op2//op1)
            if(val==2):
                st.push(op2-op1)
            if(val==1):
                st.push(op2+op1)
    print(st.top())
main()
