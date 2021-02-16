class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def InsertAtEnd(self,data):
        newNode=Node(data)
        if(self.head is None):
            self.head=newNode

        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.next=newNode
    def PrintLengthOfSinglyLinkedListRecursively(self,temp):
        if(temp is None):
            return 0
        return 1+self.PrintLengthOfSinglyLinkedListRecursively(temp.next)

    
    def PrintSinglyLinkedList(self):
        temp=self.head
        while(temp is not None):#not temp.next we need last element also
            print(temp.data,end=' ')
            
            temp=temp.next

    def deletionAtEnd(self):
        if(self.head is None):
            return
        elif(self.head.next is None):
            sel.head=None
        else:
            s1=self.head
            while(s1.next.next is not None):
                s1=s1.next

            self.tail=s1
            s1.next=None
            
    def deletionAtBeginning(self):
        if(self.head is None):
            return
        else:
            self.head=self.head.next

    def deletionAtGivenPosition(self,i):
        n=self.PrintLengthOfSinglyLinkedListRecursively(self.head)
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
    SinglyLinkedList=LinkedList()
    arr=list(map(int,input().split()))
    for i in range(len(arr)):
        SinglyLinkedList.InsertAtEnd(arr[i])

    SinglyLinkedList.PrintSinglyLinkedList()
    SinglyLinkedList.deletionAtEnd()
    SinglyLinkedList.PrintSinglyLinkedList()
    print("\n")
    SinglyLinkedList.deletionAtBeginning()
    print("\n")
    SinglyLinkedList.PrintSinglyLinkedList()
    SinglyLinkedList.deletionAtGivenPosition(2)
    SinglyLinkedList.PrintSinglyLinkedList()
if __name__=='__main__':
    main()
