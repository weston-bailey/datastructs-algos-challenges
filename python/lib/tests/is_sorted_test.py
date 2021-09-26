from unittest import TestCase, main
from ..is_sorted import is_sorted

class TestIsSorted(TestCase):
  sorted_array = [1, 2, 3, 4, 5, 6, 7, 8]
  unsorted_array = [2, 1, 4, 3, 6, 7, 5, 7]
  def test_sorted_list(self): 
    self.assertEqual(1, 1)

if __name__ == '__main__':
  main()