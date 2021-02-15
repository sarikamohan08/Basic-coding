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

    def PrintSinglyLinkedList(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=' ')
            temp=temp.next

            

def main():
    SinglyLinkedList=LinkedList()
    arr=list(map(int,input().split()))
    for i in range(len(arr)):
        SinglyLinkedList.InsertAtBeginning(arr[i])

    SinglyLinkedList.PrintSinglyLinkedList()

if __name__=='__main__':
    main()
