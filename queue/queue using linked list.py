class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class QueueUsingList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def isEmpty(self):
        return self.size==0
    
    def enqueue(self,data):
        newNode=Node(data)
        if(self.head is None):
            self.head=self.tail=newNode
            self.size+=1
            return

        self.tail.next=newNode
        self.tail=newNode
        self.size+=1
    def dequeue(self):
        if(self.isEmpty()):
            print("queue is empty")
            return
        if(self.size==1):
            temp=self.head.data
            self.head=self.tail=None
            self.size-=1
            return temp
        temp=self.head.data
        self.head=self.head.next
        self.size-=1
        return temp
    def frontele(self):
        if(self.isEmpty()):
            print("queue is empty")
            return
        return self.head.data
    def printQueue(self):
        if(self.isEmpty()):
            print("queue is empty")
            return
        temp=self.head
        while(temp is not None):
            print(temp.data,end=' ')
            temp=temp.next
        print()
        

def main():
    queue=QueueUsingList()
    for ele in input().split():
        queue.enqueue(int(ele))
    queue.printQueue()
    n=3
    while(n>0):
        print(queue.frontele())
        queue.dequeue()
        n=n-1
    queue.enqueue(100)
    queue.printQueue()
    queue.enqueue(101)
    queue.printQueue()
    queue.enqueue(102)
    queue.printQueue()
    queue.enqueue(103)
    queue.printQueue()
main()
