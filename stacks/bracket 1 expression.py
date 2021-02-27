
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

def main():
    st=Stack()
    t=int(input())
    while(t>0):
        str1=input()
        flag=1
        for ele in str1:
            if(ele=="("):
                st.push(ele)
            else:
                if(st.isEmpty()):
                    flag=0
                    break
                st.popStack()
        if(st.isEmpty() is False or flag==0):
            print("expression is unbalance")
        else:
            print("expression is balanced")
    t=t-1

if __name__=='__main__':
    main()
    
