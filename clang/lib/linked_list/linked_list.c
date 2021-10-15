#include "ll_single.h"
#include <stdio.h>

int main () 
{
  ll_single my_list = ll_single_new ();
  ll_single_push (&my_list, 10);
  ll_single_push (&my_list, 100);

  printf ("the value of my_list.head->value is %d\n", my_list.head->value);
  printf ("the value of my_list.head->next->value is %d\n", my_list.head->next->value);
  printf ("the length of my_list is %d\n", ll_single_length (my_list));
  /*
  int i;
  for (i = 0; i < 5000; i++) {
    ll_single_push (&my_list, i * i);
  }
  */
  ll_single_prepend (&my_list, 420);
  ll_single_prepend (&my_list, 420);
  ll_single_unshift (&my_list);
  ll_single_pop (&my_list);
  ll_single_print (&my_list);

  /* testing splice */

  ll_single_pop (&my_list);
  ll_single_pop (&my_list);

  ll_single_push (&my_list, 0);
  ll_single_push (&my_list, 1);
  ll_single_push (&my_list, 2);
  ll_single_push (&my_list, 3);
  ll_single_push (&my_list, 4);
  ll_single_push (&my_list, 5);
  ll_single_push (&my_list, 6);
  ll_single_push (&my_list, 7);

  ll_single_splice (&my_list, 3);

  ll_single_print (&my_list);
  printf ("sucess!\n");
  return 0;
}
