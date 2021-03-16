class QueeUsingCircularArray:
    def __init__(self,capacity):
        self.queue=[None]*capacity
        self.front=-1
        self.rear=-1
        self.size=0
        self.cap=capacity

    def isEmpty(self):
        return self.front==-1

    def enqueue(self,data):
        if((self.rear+1)%self.cap==self.front):
            print("queue is full")
            return
        if(self.isEmpty()):
            self.front=self.rear=0
            self.queue[self.rear]=data
            self.size+=1
            return
        self.rear=(self.rear+1)%self.cap
        self.queue[self.rear]=data
        self.size+=1

    def dequeue(self):
        if(self.isEmpty()):
            print("queue is empty")
            return
        if(self.rear==self.front):
            temp=self.queue[self.front]
            self.front=self.rear=-1
            return temp
        temp=self.queue[self.front]
        self.front=(self.front+1)%self.cap
        self.size-=1
        return temp

    def frontele(self):
        if(self.isEmpty()):
            print("queue is empty")
            return
        return self.queue[self.front]

    def printqueue(self):
        if(self.isEmpty()):
            print("queue is empty")
            return
        for i in range(self.size):
            print(self.queue[(self.front+i)%self.cap],end=' ')
        print()

def main():
    cap=int(input())
    queue=QueeUsingCircularArray(cap)
    for ele in input().split():
        queue.enqueue(int(ele))

    queue.printqueue()
    queue.dequeue()
    queue.printqueue()
    queue.dequeue()
    queue.printqueue()
    queue.dequeue()
    queue.printqueue()
    queue.enqueue(100)
    queue.enqueue(200)
    queue.printqueue()
    
if __name__=='__main__':
    main()
        
