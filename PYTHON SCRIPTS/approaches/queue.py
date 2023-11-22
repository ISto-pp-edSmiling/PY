#https://www.youtube.com/watch?v=D6gu-_tmEpQ
from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()
        
    def enqueue(self, node):
        self.data.append(node)           #O(1)
        
    def dequeue(self):
        self.data.popleft()              #O(1)

m = Queue()
m.enqueue(2)
m.enqueue(4)
m.dequeue()
print(m.data)