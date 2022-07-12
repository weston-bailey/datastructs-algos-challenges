'''
a stack (last in first out) data structure
'''
from dataclasses import dataclass

@dataclass
class Node:
    value: any
    next: any = None

    def __str__(self):
        return f'{self.value}'

class Stack:
    def __init__(self):
        self.head = None
        self.len = 0

    def __str__(self):
        self_str = ''
        for node in self:
            self_str += f' {node} '

        return f'[ {self_str} ]'

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __len__(self):
        return self.len

    def is_empty(self):
        '''
        returns True if the Stack is empty, False if it is not
        '''
        return len(self) == 0

    def push(self, item):
        '''
        adds item to head of the stack
        '''
        # create a new node
        new_node = Node(item)

        # if the stack is empty
        if self.is_empty():
            # set the head to be the new node 
            self.head = new_node
            # increment the length
            self.len += 1
            return

        # hold the head in a temp variable
        temp = self.head
        # set the new node to be the head
        self.head = new_node
        # set the temp variable to be the head's next
        self.head.next = temp
        # increment the length
        self.len += 1
        return

    def pop(self):
        '''
        removes item from the head of the Stack and returns it
        '''
        # if the stack is empty
        if self.is_empty():
            return None

        # store the head in a temp var
        temp = self.head
        # set the head to be the temp.next
        self.head = temp.next
        # decrement the length
        self.len -= 1
        # return the temp var
        return temp.value

    def peek(self):
        '''
        returns the head of the stack without removing it
        '''
        return self.head.value

    def contains(self, item):
        '''
        searches for the item in the stack and returns True or False based on
        whether it is found
        '''
        pass
