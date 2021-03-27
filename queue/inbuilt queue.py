from queue import Queue
from queue import LifoQueue

q=Queue(maxsize=10)
q.put(10)
q.put(20)
q.put(30)
q.put(40)
q.put(50)
q.put(60)
q.put(70)
q.put(80)
q.put(90)
q.put(100)
print(q.empty())
print(q.full())
print(q.qsize())
#q.put(110)

while(q.empty() is False):
    print(q.get())
