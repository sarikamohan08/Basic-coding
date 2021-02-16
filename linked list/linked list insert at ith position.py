class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def InsertAtBeginning(self,data):
        newNode=Node(data)
        if(self.head is None):
            self.head=newNode
            
        else:
            newNode.next=self.head
            self.head=newNode
            
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

    def PrintSinglyLinkedList(self):
        temp=self.head
        while(temp is not None):#not temp.next we need last element also
            print(temp.data,end=' ')
            
            temp=temp.next

    def PrintLengthOfSinglyLinkedList(self):
        temp=self.head
        count=0
        while(temp is not None):
            count+=1
            temp=temp.next
        return count
    
    def PrintLengthOfSinglyLinkedListRecursively(self,temp):
        if(temp is None):
            return 0
        return 1+self.PrintLengthOfSinglyLinkedListRecursively(temp.next)
        

def main():
    SinglyLinkedList=LinkedList()
    arr=list(map(int,input().split()))
    for i in range(len(arr)):
        SinglyLinkedList.InsertAtBeginning(arr[i])
    SinglyLinkedList.InsertAtPosition(4,100)
    
    SinglyLinkedList.PrintSinglyLinkedList()
    print(SinglyLinkedList.PrintLengthOfSinglyLinkedList())
    temp=SinglyLinkedList.head
    print(SinglyLinkedList.PrintLengthOfSinglyLinkedListRecursively(temp))
    
if __name__=='__main__':
    main()
