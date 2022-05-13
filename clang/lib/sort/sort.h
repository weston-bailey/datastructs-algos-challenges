#include <stdio.h>
int is_sorted(int *array, size_t length);
void print_nums(int *numbers, size_t len);

int is_sorted(int *array, size_t length)
{
  for (int i = 0; i < length; i++)
  {
    if (array[i] > array[i + 1])
    {
      return 0;
    }
  }
  return 1;
}

void print_nums(int *numbers, size_t len)
{
  int i = 0;
  printf("int numbers[] = {");
  for (i = 0; i < len; i++)
  {
    printf(" %d, ", numbers[i]);
  }
  printf("};\n");
}