from unittest import unittest
from Queue import Queue

class TestQueue:
    def test_is_empty(self):
        """
        should return True when queue is empty and False when it is not
        """
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(0)
        self.assertFalse(q.is_empty())
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_enqueue(self):
        """
        should add a item to the end of the queue, and increase the length
        """
        q = Queue()
        # insertion when empty
        q.enqueue(0)
        self.assertEqual(1, len(q))
        self.assertEqual(0, q.head.value)
        self.assertEqual(0, q.tail.value)
        # insertion when there is one item
        q.enqueue(1)
        self.assertEqual(2, len(q))
        self.assertEqual(0, q.head.value)
        self.assertEqual(1, q.head.next.value)
        self.assertEqual(1, q.tail.value)
        # insertion when there is more than one item
        q.enqueue(2)
        self.assertEqual(3, len(q))
        self.assertEqual(0, q.head.value)
        self.assertEqual(1, q.head.next.value)
        self.assertEqual(2, q.head.next.next.value)
        self.assertEqual(2, q.tail.value)

    def test_dequeue(self):
        """
        should remove the item from the beginning of the queue and decrement
        the length
        """
        q = Queue()
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        test = q.deqeue()
        self.assertEqual(test, 0)
        self.assertEqual(2, len(q))
        test = q.deqeue()
        self.assertEqual(test, 1)
        self.assertEqual(1, len(q))
        test = q.deqeue()
        self.assertEqual(test, 2)
        self.assertEqual(0, len(q))
        self.assertIsNone(q.head)
        self.assertIsNone(q.tail)

    def test_peek(self):
        """
        should return the next up to be dequeued, but not remove it
        """
        q = Queue()
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        test = q.peek()
        self.assertEqual(test, 0)
        self.assertEqual(3, len(q))
        q.dequeue()
        test = q.peek()
        self.assertEqual(test, 1)
        self.assertEqual(2, len(q))
        q.dequeue()
        test = q.peek()
        self.assertEqual(test, 2)
        self.assertEqual(1, len(q))
        d.dequeue()
        test = q.peek()
        self.assertIsNone(test)
if __name__ == '__main__':
    main()
