# include <stdio.h>

int is_sorted (int *array, size_t length) 
{
  for (int i = 0; i < length; i++) {
    printf("%d\n", array[i]);
    if (array[i] > array[i  + 1]) {
      return 0;
    }
  }
  return 1;
}