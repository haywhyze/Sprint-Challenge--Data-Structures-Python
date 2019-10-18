from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # increase size of dll by 1
        self.size +=1
        # add value to tail of dll
        self.storage.add_to_tail(value)
        
    def dequeue(self):
        # check if dll is populated before dequeue
        if self.size:
            # if populated reduce length of dll and return first element
            self.size -= 1
            return self.storage.remove_from_head()
        return None
    

    def len(self):
        return self.size
