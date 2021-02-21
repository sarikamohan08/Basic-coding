class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def InsertAtEnd(self,data):
        newNode=Node(data)
        if(self.head is None):
            self.head=newNode
            self.tail=newNode
            self.tail.next=self.head
            return

        else:
            newNode.next=self.head
            self.tail=newNode
            self.tail.next=self.head
            
    
    def InsertAtBeginning(self,data):
        newNode=Node(data)
        if(self.head is None):
            self.head=newNode
            self.tail=newNode
            self.tail.next=self.head
            return
            
        else:
            newNode.next=self.head
            self.head=newNode
            self.tail.next=self.head
            
            
    def InsertAtPosition(self,i,data):
        newNode=Node(data)
        if(i==0):
            self.InsertAtBeginning(data)

        else:
            count=0
            temp=self.head
            while(temp.next is not None and count is not i-1):
                count+=1
                temp=temp.next
            if(temp.next is None and i>count+1):
                return
            else:
                newNode.next=temp.next
                temp.next=newNode
            temp.next=newNode

    def PrintCircularSinglyLinkedList(self):
        temp=self.head
        while(True):#not temp.next we need last element also
            print(temp.data,end=' ')
            temp=temp.next
            if(temp==self.head):
                break
    def PrintLengthOfSinglyLinkedList(self,head):
        temp=self.head
        count=0
        while(True):
            count+=1
            temp=temp.next
            if(temp==self.head):
                break
        return count
    def deletionAtEnd(self):
        if(self.head is None):
            return
        elif(self.head.next is None):
            self.head=None
            self.tail=None
            return
        else:
            s1=self.head
            while(s1.next is not self.tail):
                s1=s1.next

            self.tail.next=None
            self.tail=s1
            self.tail.next=self.head
            
    def deletionAtBeginning(self):
        if(self.head is None):
            self.head=None
            self.tail=None
            return
        else:
            self.head=self.head.next
            self.tail.next=self.head
            
    def deletionAtGivenPosition(self,i):
        n=self.PrintLengthOfSinglyLinkedList(self.head)
        if(self.head is None or i>n-1):
            return
        if(i==0):
            self.deletionAtBeginning()
            return
        if(i==n-1):
            self.deletionAtEnd()
            
        count=0
        temp=self.head
        while(temp is not None and count is not (i-1)):
            count+=1
            temp=temp.next
        temp.next=temp.next.next
def main():
    CircularSinglyLinkedList=CircularLinkedList()
    arr=list(map(int,input().split()))
##    for i in range(len(arr)):
##        CircularSinglyLinkedList.InsertAtEnd(arr[i])

    for i in range(len(arr)):
        CircularSinglyLinkedList.InsertAtBeginning(arr[i])
    CircularSinglyLinkedList.PrintCircularSinglyLinkedList()
    print()
    CircularSinglyLinkedList.InsertAtPosition(1,8)
    CircularSinglyLinkedList.PrintCircularSinglyLinkedList()
    CircularSinglyLinkedList.deletionAtEnd()
    CircularSinglyLinkedList.PrintCircularSinglyLinkedList()
    print()
    CircularSinglyLinkedList.deletionAtBeginning()
    print()
    CircularSinglyLinkedList.PrintCircularSinglyLinkedList()
    CircularSinglyLinkedList.deletionAtGivenPosition(2)
    CircularSinglyLinkedList.PrintCircularSinglyLinkedList()

if __name__=='__main__':
    main()
