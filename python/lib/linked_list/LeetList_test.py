from .LeetList import LeetList
from unittest import TestCase, main

class LeetListName(TestCase):
    def test_add(self):
        '''
            tests adding values to the list
        '''
        l = LeetList()
        l.add(10).add(50).add(100)
        self.assertEqual(l.head.val, 10)
        self.assertEqual(l.head.next.val, 50)
        self.assertEqual(l.head.next.next.val, 100)

if __name__ == '__main__':
    main()
