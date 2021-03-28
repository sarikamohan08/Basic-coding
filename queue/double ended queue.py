class Deque():
    def __init__(self):
        self._dq=[]

    def isEmpty(self):
        return self._dq==[]

    def insertRear(self,data):
        self._dq.append(Data)

    def insertFront(self,data):
        self._dq.insert(0,data)

    def deleteRear(self):
        self._dq.pop()

    def deleteFront(self):
        self._dq.pop(0)

    def size(self):
        return len(self._dq)

    def frontEle(self):
        return self._dq[0]

    def rearEle(self):
        return self._dq[-1]

    def printDeque(self):
        for ele in self._dq:
            print(ele,end=' ')
        print()

def main():
    deque=Deque()
    deque.insertFront(10)
    deque.printDeque()
    deque.insertFront(20)
    deque.printDeque()
    deque.insertFront(30)
    deque.printDeque()
    deque.insertFront(40)
    deque.printDeque()
    deque.insertFront(50)
    deque.printDeque()
    deque.insertFront(60)
    deque.printDeque()
    deque.insertFront(70)
    deque.printDeque()
    deque.insertFront(80)
    deque.printDeque()
    print(deque.frontEle())
    print(deque.rearEle())

    deque.deleteRear()
    deque.deleteFront()

    print(deque.size())
    print(deque.isEmpty())

main()
