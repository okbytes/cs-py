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
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from singly_linked_list import LinkedList

"""
Using my Linked Lists
"""


class Queue:
    def __init__(self):
        self.storage = LinkedList()
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()


"""
Using Python Lists
"""


# class QueuePythonLists:
#     def __init__(self):
#         self.storage = []
#         self.size = 0

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size = len(self.storage)

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             ret_val = self.storage[0]

#             if self.size == 1:
#                 self.storage = []
#             else:
#                 self.storage = self.storage[1:]

#             self.size = len(self.storage)
#             return ret_val