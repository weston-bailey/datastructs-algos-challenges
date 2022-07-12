from unittest import TestCase, main
from .Stack import Stack

class TestStack(TestCase):
    def test_is_empty(self):
        '''
        Stack.is_empty() should return True when the stack is empty and False when it is not
        '''
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(0)
        self.assertFalse(s.is_empty())
        s.pop()
        self.assertTrue(s.is_empty())

    def test_push(self):
        '''
        Stack.push() should add an item to the head to the head of the stack
        '''
        pass

    def test_pop(self):
        '''
        Stack.pop() should remove the head item from the stack and return it
        '''
        pass

    def test_peep(self):
        '''
        Stack.peep() should return the head without removing it
        '''
        pass

    def test_contains(self):
        '''
        Stack.cotains() should return a bool if the stack contains the item
        '''
        pass

if __name__ == '__main__':
    main()
