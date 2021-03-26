class QueueUsingList:
    def __init__(self):
        self.queue=[]
        self.size=0
        self.front=0

    def enqueue(self,data):
        self.queue.append(data)
        self.size+=1
        
    def isEmpty(self):
        return self.size==0
    
    def dequeue(self):
        if(self.isEmpty()):
            print("queue is empty")
            return
        temp=self.queue[self.front]
        self.front+=1
        self.size-=1
        return temp
    
    def frontele(self):
        if(self.isEmpty()):
            print("queue is empty")
            return
        return self.queue[self.front]
    def printQueue(self):
        if(self.isEmpty()):
            print("queue is empty")
            return
        for i in range(self.size):
            print(self.queue[self.front+i],end= ' ')
        print()
class Stack:
    def __init__(self):
        self.arr=[]
        self.tos=-1

    def push(self,data):
        self.tos+=1
        self.arr.append(data)

    def pop(self):
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
def reverseKEle(queue,st,k):
    if(queue.isEmpty() or k>queue.size or k<=0):
        return
    for i in range(k):
        st.push(queue.dequeue())
    while(st.isEmpty() is False):
        queue.enqueue(st.top())
        st.pop()
    for i in range(queue.size-k):
        queue.enqueue(queue.dequeue())
        
def main():
    queue=QueueUsingList()
    st=Stack()
    for ele in input().split():
        queue.enqueue(int(ele))
    k=int(input())
    reverseKEle(queue,st,k)
    queue.printQueue()
main()
