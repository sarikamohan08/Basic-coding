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
            
    def InsertAtPosition(self,data):
        if self.head is None: 
            new_node.next = self.head 
            self.head = new_node 
  
        # Special case for head at end 
        elif self.head.data >= new_node.data: 
            new_node.next = self.head 
            self.head = new_node 
  
        else : 
  
            # Locate the node before the point of insertion 
            current = self.head 
            while(current.next is not None and
                 current.next.data < new_node.data): 
                current = current.next
              
            new_node.next = current.next
            current.next = new_node 

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
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    k=list(map(int,input().split()))
    for i in range(len(arr)):
        SinglyLinkedList.InsertAtBeginning(arr[i])
    SinglyLinkedList.InsertAtPosition(k)
    
    SinglyLinkedList.PrintSinglyLinkedList()
    print(SinglyLinkedList.PrintLengthOfSinglyLinkedList())
    temp=SinglyLinkedList.head
    print(SinglyLinkedList.PrintLengthOfSinglyLinkedListRecursively(temp))
    
if __name__=='__main__':
    main()

