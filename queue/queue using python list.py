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
