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

    def PrintSinglyLinkedList(self):
        temp=self.head
        while(temp is not None):#not temp.next we need last element also
            print(temp.data,end=' ')
            print(temp,end=' ')
            print(temp.next)
            temp=temp.next

            

def main():
    SinglyLinkedList=LinkedList()
    arr=list(map(int,input().split()))
    for i in range(len(arr)):
        SinglyLinkedList.InsertAtEnd(arr[i])

    SinglyLinkedList.PrintSinglyLinkedList()

if __name__=='__main__':
    main()
