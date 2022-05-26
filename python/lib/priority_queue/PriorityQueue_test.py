from unittest import TestCase, main
from lib.priority_queue.PriorityQueue import PriorityQueue

class TestPriorityQueue(TestCase):
    def test_is_empty(self):
        q = PriorityQueue()
        self.assertFalse(q.is_empty())
        q.insert(10)

        self.assertTrue(q.is_empty())

if __name__ == '__main__':
    main()
