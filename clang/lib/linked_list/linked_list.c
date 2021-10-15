#include "sll.h"
#include <stdio.h>

int main () 
{
  sll my_list = sll_new ();
  sll_push (&my_list, 10);
  sll_push (&my_list, 100);

  printf ("the value of my_list.head->value is %d\n", my_list.head->value);
  printf ("the value of my_list.head->next->value is %d\n", my_list.head->next->value);
  printf ("the length of my_list is %d\n", sll_length (my_list));
  /*
  int i;
  for (i = 0; i < 5000; i++) {
    sll_push (&my_list, i * i);
  }
  */
  sll_prepend (&my_list, 420);
  sll_prepend (&my_list, 420);
  sll_unshift (&my_list);
  sll_pop (&my_list);
  sll_print (&my_list);

  /* testing splice */

  sll_pop (&my_list);
  sll_pop (&my_list);

  sll_push (&my_list, 0);
  sll_push (&my_list, 1);
  sll_push (&my_list, 2);
  sll_push (&my_list, 3);
  sll_push (&my_list, 4);
  sll_push (&my_list, 5);
  sll_push (&my_list, 6);
  sll_push (&my_list, 7);

  printf ("the length of my_list is %d\n", sll_length (my_list));
  sll_splice (&my_list, 3, 1000);

  sll_print (&my_list);
  printf ("sucess!\n");
  return 0;
}
