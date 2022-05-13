from unittest import TestCase, main
from ....lib.data.random_list import random_list
from ....lib.sort.bubble_sort import *
from ....lib.sort.is_sorted import *
from ....lib.sort.insertion_sort import *
from ....lib.sort.selection_sort import *
from ....lib.sort.bucket_sort import *
from ....lib.sort.heap_sort import *
from ....lib.sort.merge_sort import *
from ....lib.sort.quick_sort import *


class Test_Sorts(TestCase):

    def test_bubble_sort_1(self):
        # test simple list
        unsorted_list = [2, 1, 4, 3, 6, 7, 5, 7]
        sorted_list = bubble_sort_1(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)
        # test random complex list
        unsorted_list = random_list(length=500, negative=True)
        sorted_list = bubble_sort_1(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)

    # these are current;y failing

    # def test_bubble_sort_2(self):
    #   unsorted_list = [2, 1, 4, 3, 6, 7, 5, 7]
    #   sorted_list = bubble_sort_2(unsorted_list)
    #   sorted_test = is_sorted(sorted_list)
    #   self.assertTrue(sorted_test)

    # def test_bubble_sort_3(self):
    #   unsorted_list = [2, 1, 4, 3, 6, 7, 5, 7]
    #   sorted_list = bubble_sort_3(unsorted_list)
    #   sorted_test = is_sorted(sorted_list)
    #   self.assertTrue(sorted_test)

    def test_insertion_sort(self):
        # test simplle list
        unsorted_list = [2, 1, 4, 3, 6, 7, 5, 7]
        sorted_list = insertion_sort(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)
        # test random complex list
        unsorted_list = random_list(length=500, negative=True)
        sorted_list = insertion_sort(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)

    # def test_insertion_sort_2(self):
    #   unsorted_list = [2, 1, 4, 3, 6, 7, 5, 7]
    #   sorted_list = insertion_sort_2(unsorted_list)
    #   sorted_test = is_sorted(sorted_list)
    #   self.assertTrue(sorted_test)

    def test_selection_sort(self):
        # test simplle list
        unsorted_list = [2, 1, 4, 3, 6, 7, 5, 7]
        sorted_list = selection_sort(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)
        # test random complex list
        unsorted_list = random_list(length=500, negative=True)
        sorted_list = selection_sort(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)

    def test_bucket_sort(self):
        # test simplle list
        unsorted_list = [2, 1, 4, 3, 6, 7, 5, 7]
        sorted_list = bucket_sort(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)
        # test random complex list
        unsorted_list = random_list(length=500)
        sorted_list = bucket_sort(unsorted_list, num_buckets=10)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)
        #  test bucket_sort with another sort algo
        unsorted_list = random_list(length=500)
        sorted_list = bucket_sort(
            unsorted_list, num_buckets=10, sort_algorithm=selection_sort)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)

    def test_heap_sort(self):
        # test simplle list
        unsorted_list = [2, 1, 4, 3, 6, 7, 5, 7]
        sorted_list = heap_sort(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)
        # test random complex list
        unsorted_list = random_list(length=500)
        sorted_list = heap_sort(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)

    def test_merge_sort(self):
        # test simplle list
        unsorted_list = [2, 1, 4, 3, 6, 7, 5, 7]
        sorted_list = merge_sort(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)
        # test random complex list
        unsorted_list = random_list(length=500)
        sorted_list = merge_sort(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)

    def test_quick_sort(self):
        # test simplle list
        unsorted_list = [2, 1, 4, 3, 6, 7, 5, 7]
        sorted_list = quick_sort(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)
        # test random complex list
        unsorted_list = random_list(length=500)
        sorted_list = quick_sort(unsorted_list)
        sorted_test = is_sorted(sorted_list)
        self.assertTrue(sorted_test)


if __name__ == '__main__':
    main()
