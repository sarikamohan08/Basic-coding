
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

def precedence(str1):
    if(str1=="^"):
        return 3
    if(str1=="*"or str1=="/"):
        return 2
    if(str1=="+" or str=="-"):
        return 1
    if(str==")" or str=="("):
        return -1
    else:#if operand returning statement
        return 0
def main():
    st=Stack()
    arr=list(input().split())
    ans=""
    for i in range(len(arr)):
        val=precedence(arr[i])
        if(val==0):
            ans+=arr[i]
        else:
            if(arr[i]=="("):
                st.push(arr[i])
                
            elif(arr[i]==")"):
                while(st.isEmpty() is False and st.top()!="("):
                    ans+=st.top()
                    st.popStack()
                    
                if(st.top()=="("):
                    st.popStack()
            else:#if arr[i] is operator
                while(st.isEmpty is False and precedence(arr[i])<=precedence(st.top())):
                    ans+=st.top()
                    st.pop()
                st.push(arr[i])
                
    while(st.isEmpty() is False):
        ans+=st.top()
        st.popStack()
        
    print(ans)
if __name__=='__main__':
    main()
    
