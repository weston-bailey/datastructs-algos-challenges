from unittest import TestCase, main
from .binary_search import search

class Test_Search(TestCase):
    def test_is_mid_in_list(self):
        target = 3
        nums = [1, 2, 3, 4, 5]
        result = search(nums, target)
        output = 2
        self.assertEqual(result, output)

    def test_exists_in_list(self):
        target = 9
        nums = [-1,0,3,5,9,12]
        result = search(nums, target)
        output = 4
        self.assertEqual(result, output)

    def test_does_not_exist_in_list(self):
        target = 2
        nums = [-1,0,3,5,9,12]
        result = search(nums, target)
        output = -1
        self.assertEqual(result, output)

    def test_first_in_list(self):
        target = -1
        nums = [-1,0,3,5,9,12]
        result = search(nums, target)
        output = 0
        self.assertEqual(result, output)

    def test_last_in_list(self):
        target = 12
        nums = [-1,0,3,5,9,12]
        result = search(nums, target)
        output = 5
        self.assertEqual(result, output)

if __name__ == '__main__':
    main()

