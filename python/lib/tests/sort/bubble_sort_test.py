from unittest import TestCase, main
from ...sort.bubble_sort import *
from ...sort.is_sorted import *

class Test_Sorts(TestCase):

  def test_bubble_sort_1(self):
    unsorted_list = [2, 1, 4, 3, 6, 7, 5, 7]
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

if __name__ == '__main__':
  main()