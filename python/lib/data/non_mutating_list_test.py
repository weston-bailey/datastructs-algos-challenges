from unittest import TestCase, main
from lib.data.non_mutated_list import non_mutated_list
from lib.data.random_list import random_list
from lib.sort.is_sorted import is_sorted
from lib.sort.selection_sort import selection_sort

class Test_Non_Mutated_List(TestCase):
    def test_type(self):
        # should return a list
        unsorted_list = random_list(length=500)
        sorted_list = non_mutated_list(unsorted_list, selection_sort)
        sorted_test = is_sorted(sorted_list)
        self.assertIsInstance(sorted_list, list)

    def test_sorted(self):
        # should retrun a sorted list
        unsorted_list = random_list(length=500)
        sorted_list = non_mutated_list(unsorted_list, selection_sort)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)

    def test_unordered(self):
        # should not mutate original list
        unsorted_list = random_list(length=500)
        non_mutated_list(unsorted_list, selection_sort)
        unsorted_test = is_sorted(unsorted_list)
        self.assertFalse(unsorted_test)


if __name__ == '__main__':
    main()
