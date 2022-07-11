"""
A Queue implementation that uses a linked list
"""
from dataclasses import dataclass

@dataclass
class Node:
    value: any
    next: any = None

    def __repr__(self):
        return str(value)

class Queue:
    """
    A queue FIFO datasctructure implemented with a linked list
        Params:
            head: Node = the first in, will be out next
            tail: Node = the last in, will be out last
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node

            current_node = current_node.next

    def __str__(self):
        self_str = ''
        for node in self:
            self_str += f' {node.value} '

        return f' [ {self_str} ]'

    def __len__(self):
        return self.len

    def is_empty(self):
        """
        returns true if queue is empty, false if not

        """
        return len(self) == 0

    def enqueue(self, item):
        """
        adds item to tail of queue
        """
        # create a new node
        new_node = Node(item)

        # if this is the first thing added to the queue
        if len(self) == 0:
            # set the head and the tail to be the new node
            self.head  = new_node
            self.tail = new_node
            self.len += 1
            return True

        # store the tail in a temp variable
        temp = self.tail
        # set the tail to be the new node
        self.tail = new_node
        # set the temp's next to be the new node
        temp.next = new_node
        # increment the size of the queue
        self.len += 1
        return True

    def dequeue(self):
        """
        removes item from head of the queue, and returns it
        """
        # account for queue being empty
        if len(self) == 0:
            return None

        # store the head in a temp variable
        temp = self.head

        # if there is only one thing in the queue
        if len(self) == 1:
            # set the head and tail to be None
            self.head = None
            self.tail = None
            # decrement the size of the queue
            self.len -= 1
            # return the temp
            return temp

        # set the head's next to be the head
        self.head = temp.next
        # decrement the length 
        self.len -= 1
        # return the temp varaible
        return temp


    def peek(self):
        """
        returns the first item in the queue, but does not remove it
        """
        return self.head

def main():
    q = Queue()
    print(len(q))
    print(q)

if __name__ == '__main__':
    main()
