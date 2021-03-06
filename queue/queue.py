"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

   Head and tail are reversed.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""



"""
QUEUE — ARRAY/LIST
"""
#class Queue:
#    def __init__(self):
#        self.size = 0
#        self.storage = []

#    def __len__(self):
#        return self.size

#    def enqueue(self, value):
#        self.storage.insert(0, value)
#        self.size += 1

#    def dequeue(self):
#        if len(self.storage) == 0:
#            return None
#        else:
#            last_value = self.storage[-1]
#            self.storage.pop(-1)
#            self.size -= 1
#            return last_value

"""
QUEUE — SINGLY LINKED LIST
"""
from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        try:
            val = self.storage.head.value
            self.storage.remove_head()
            self.size -= 1
            return val
        except:
            return None