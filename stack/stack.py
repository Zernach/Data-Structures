"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

"""
STACK — ARRAY/LIST
"""
#class Stack:
#    def __init__(self):
#        self.size = 0
#        self.storage = []

#    def __len__(self):
#        return self.size

#    def push(self, value):
#        self.storage.insert(0, value)
#        self.size += 1

#    def pop(self):
#        if len(self.storage) == 0:
#            return None
#        else:
#            value = self.storage[0]
#            self.storage.remove(value)
#            self.size -= 1
#            return value

"""
STACK — USING SINGLY LINKED LIST
"""
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        try:
            val = self.storage.head.value
            self.storage.remove_head()
            self.size -= 1
            return val
        except:
            return None