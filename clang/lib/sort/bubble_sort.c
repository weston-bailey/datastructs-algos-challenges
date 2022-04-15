#include <stddef.h>
#include <stdio.h>
#include "sort.h"

int bubble_sort (int *numbers, size_t len);

int main (int argc, char *argv[])
{
  int numbers[] = { 7, 3, 1, 5, 6, 3, 7 };
  size_t len = sizeof (numbers) / sizeof (int);

  print_nums (numbers, len);
  
  bubble_sort (numbers, len);

  print_nums (numbers, len);

  char *sorted = is_sorted (numbers, len) ? "Yes" : "No";
  
  printf ("Is it sorted? %s.\n", sorted);
  return 0;
}


int bubble_sort (int *numbers, size_t len)
{

  int i = 0;
  int made_swap = 0;
  do {
    made_swap = 0;
    for (i = 0; i < len; i++) {
      if (numbers[i] > numbers[i + 1]) {
	int temp = numbers[i];
	numbers[i] = numbers[i +1];
	numbers[i + 1] = temp;
	made_swap = 1;
      }
    }
  
  } while (made_swap);

  return 1;
}
