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
        s = Stack()
        s.push(0)
        self.assertEqual(0, s.head.value)
        self.assertEqual(1, len(s))
        s.push(1)
        self.assertEqual(1, s.head.value)
        self.assertEqual(2, len(s))
        s.push(2)
        self.assertEqual(2, s.head.value)
        self.assertEqual(3, len(s))

    def test_pop(self):
        '''
        Stack.pop() should remove the head item from the stack and return it
        '''
        s = Stack()
        s.push(0)
        s.push(1)
        s.push(2)
        test = s.pop()
        self.assertEqual(2, test)
        test = s.pop()
        self.assertEqual(1, test)
        test = s.pop()
        self.assertEqual(0, test)
        test = s.pop()
        self.assertIsNone(test)

    def test_peek(self):
        '''
        Stack.peek() should return the head without removing it
        '''
        s = Stack()
        s.push(10)
        s.push(11)
        self.assertEqual(11, s.peek())
        self.assertEqual(11, s.peek())
        self.assertEqual(11, s.peek())

    def test_contains(self):
        '''
        Stack.cotains() should return a bool if the stack contains the item
        '''
        pass

if __name__ == '__main__':
    main()
