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
        
def reverse(queue):
    if(queue.isEmpty()):
        return
    temp=queue.dequeue()
    reverse(queue)
    queue.enqueue(temp)

def main():
    queue=QueueUsingList()
    for ele in input().split():
        queue.enqueue(int(ele))
    reverse(queue)
    queue.printQueue()
main() 
