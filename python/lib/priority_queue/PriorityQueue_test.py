from unittest import TestCase, main
from lib.priority_queue.PriorityQueue import PriorityQueue

class TestPriorityQueue(TestCase):
    '''
        Tests PriorityQueue methods
    '''
    def test_is_empty(self):
        '''
            PriorityQueue.is_empty() should return false when the queue is empty and true when the queue is empty
        '''

        q = PriorityQueue()
        self.assertTrue(q.is_empty())
        q.insert(10)

        self.assertFalse(q.is_empty())

    def test_len(self):
        '''
           len(PriorityQueue) should return the length of the queue
        '''
        q = PriorityQueue()
        self.assertEqual(0, len(q))
        q.insert(1)
        self.assertEqual(1, len(q))
        q.insert(2)
        self.assertEqual(2, len(q))

    def test_insert(self):
        '''
            PriorityQueue.insert(data) should add a new data value last in the queue
        '''
        q = PriorityQueue()
        q.insert(10)
        self.assertFalse(q.is_empty())
        self.assertEqual(1, len(q))
        self.assertEqual(10, q.peek())

    def test_clear(self):
        '''
            PriorityQueue.clear() should completely empty the queue
        '''
        q = PriorityQueue()
        q.insert(10)
        q.insert(20)
        q.clear()
        self.assertTrue(q.is_empty())

    def test_peek(self):
        '''
            PriorityQueue.peek() should return the head of the queue but not remove it
        '''
        q = PriorityQueue()
        q.insert(10)
        self.assertEqual(10, q.peek())
        q.insert(20)
        self.assertEqual(10, q.peek())

    def test_poll(self):
        '''
            PriorityQueue.poll() should remove the the head of the queue and retrieve it
        '''
        q = PriorityQueue()
        q.insert(10)
        q.insert(20)
        q.insert(30)
        self.assertEqual(10, q.poll())
        self.assertEqual(20, q.poll())
        self.assertEqual(30, q.poll())

    def test_add(self):
        '''
            PriorityQueue.add() should add data at specific priorirties
        '''
        q = PriorityQueue()
        q.insert(10)
        q.insert(20)
        q.insert(30)
        q.add(5, 0)
        self.assertEqual(5, q.peek())

    def test_contains(self):
        '''
            PriorityQueue.contains() should return true if queue contains a value, false if not
        '''
        q = PriorityQueue()
        q.insert(10)
        q.insert(20)
        q.insert(30)
        self.assertTrue(q.contains(10))
        self.assertFalse(q.contains(45))

if __name__ == '__main__':
    main()
