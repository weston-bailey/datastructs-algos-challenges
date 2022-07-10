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

    def __repr__(self):
        pass

    def __len__(self):
        pass

    def is_empty(self):
        """
        returns true if queue is empty, false if not

        """
        pass

    def enqueue(self, item):
        """
        adds item to tail of queue
        """
        pass

    def dequeue(self):
        """
        removes item from head of the queue, and returns it
        """
        pass

    def peek(self):
        """
        returns the first item in the queue, but does not remove it
        """
        pass
