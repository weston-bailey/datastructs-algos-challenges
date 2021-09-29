from unittest import TestCase, main
from ....lib.sort.is_sorted import is_sorted

class TestIsSorted(TestCase):

  def test_sorted_list(self): 
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]
    self.assertTrue(is_sorted(sorted_list))

  def test_unsorted_list(self):
    unsorted_list = [2, 1, 4, 3, 6, 7, 5, 7]
    self.assertFalse(is_sorted(unsorted_list))

if __name__ == '__main__':
  main()