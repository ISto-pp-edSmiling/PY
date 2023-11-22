#https://www.youtube.com/watch?v=KcT3aVgrrpU
# a stack is not a heap!
# code for stack

class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, node):
        self.data.append(node)          #O(1)
    
    def pop(self):
        self.data.pop()                 #O(1)