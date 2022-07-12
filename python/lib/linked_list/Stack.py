'''
a stack (last in first out) data structure
'''
from dataclasses import dataclass

@dataclass
class Node:
    pass

class Stack:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def is_empty(self):
        '''
        returns True if the Stack is empty, False if it is not
        '''
        pass

    def push(self, item):
        '''
        adds item to head of the stack
        '''
        pass

    def pop(self):
        '''
        removes item from the head of the Stack and returns it
        '''
        pass

    def peek(self):
        '''
        returns the head of the stack without removing it
        '''
        pass

    def contains(self, item):
        '''
        searches for the item in the stack and returns True or False based on
        whether it is found
        '''
        pass
