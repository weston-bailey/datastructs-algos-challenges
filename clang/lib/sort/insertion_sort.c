#include <stdlib.h>
#include "sort.h"

void insertion_sort (int *nums, size_t len)
{

  // loop over the nums
  int i = 0;
  for (i = 0; i < len; i++) {
    int j = i;
    while (nums[j] < nums[j - 1] && j > 0) {
      int swap = nums[j];
      nums[j] = nums[j - 1];
      nums[j - 1] = swap;
      j--;
    }
  }
}

int main (int argc, char *argv[])
{
  int nums[] = { 3, 4, 1, 6, 7, 9, 5, 6, 2, 8 };
  size_t len = sizeof (nums) / sizeof (int);
  insertion_sort (nums, len);

  char *sort_status = is_sorted (nums, len) ? "Yes" : "No";
  printf ("Are the nums sorted? %s.\n", sort_status);

  print_nums (nums, len);
  return 0;
}
