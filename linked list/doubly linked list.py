class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insertAtEnd(self,data):
        newNode=Node(data)
        if(self.head is None):
            self.head=newNode
            self.tail=newNode
            return

        self.tail.next=newNode
        newNode.prev=self.tail
        self.tail=newNode

    def insertAtBegining(self,data):
        newNode=Node(data)
        if(self.head is None):
            self.head=newNode
            self.tail=newNode
            return

        newNode.next=self.head
        self.head.prev=newNode
        
        self.head=newNode
        
    def insertAtMiddle(self,i,data):
        newNode=Node(data)
        n=self.length()
        if(i==0):
            self.insertAtBegining(data)
            return
        if(i==n):
            self.insertAtEnd(data)
            return
        if(i>n):
            print("invalid")
            return
        count=0
        temp=self.head
        while(temp.next is not None and count is not (i-1)):
             count+=1
             temp=temp.next
        newNode.prev=temp
        newNode.next=temp.next
        temp.next.prev=newNode
        temp.next=newNode

    def print(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=' ')
            temp=temp.next
        print()

        
    def length(self):
        temp=self.head
        count=0
        while(temp is not None):
            count+=1
            temp=temp.next
        return count
    def deleteAtBeginning(self):
        if(self.head is None):
            print("linked list is empty")
            return
        temp=self.head.next
        if(temp is None):
            self.head=None
            return
        
        self.head.next=None
        temp.prev=None
        self.head=temp
        
    def deletionAtEnd(self):
        if(self.head is None):
            print("linked list is empty")
            return
        temp=self.tail.prev
        temp.next=None
        temp.prev=None
        temp=self.tail
        
    def deletionAtMiddle(self,i):
        if(self.head is None):
            print("linked list is empty")
            return
        n=self.length()
        if(i==0):
            self.deletionAtBeginning(data)
            return
        if(i==n):
            self.deletionAtEnd(data)
            return
        if(i>n):
            print("invalid")
            return
        count=0
        temp=self.head
        while(temp.next is not None and count is not (i-1)):
             count+=1
             temp=temp.next
        temp1=temp.prev
        temp2=temp.next
        temp.prev=None
        temp.next=None
        temp1.next=temp2
        temp2.prev=temp1
        
def main():
    doublyLinkedList=DoublyLinkedList()
    arr=list(map(int,input().split()))
##    for i in range(len(arr)):
##        doublyLinkedList.insertAtEnd(arr[i])
##    doublyLinkedList.print()
    for i in range(len(arr)):
        doublyLinkedList.insertAtBegining(arr[i])
    doublyLinkedList.print()
    doublyLinkedList.insertAtMiddle(2,9)
    doublyLinkedList.print()
    doublyLinkedList.insertAtMiddle(1,10)
    doublyLinkedList.print()
    doublyLinkedList.deleteAtBeginning()
    doublyLinkedList.print()
    doublyLinkedList.deletionAtEnd()
    doublyLinkedList.print()
    doublyLinkedList.deletionAtMiddle(5)
    doublyLinkedList.print()
    

if __name__=='__main__':
    main()
