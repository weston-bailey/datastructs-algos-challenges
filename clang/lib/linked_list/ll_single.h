#ifndef LL_SINGLE
#define LL_SINGLE
#include <stddef.h>
#include <stdlib.h>


typedef struct LL_Single ll_single;
typedef struct LL_Single_Node ll_single_node;
typedef int ll_single_value;

ll_single new_ll_single ();

/* linked list manager struct */
struct LL_Single {
  /* the first node in the head of the liked list */
  ll_single_node *head;
  /* the node that is currently being checked */
  ll_single_node *current;
  /* the number of nodes in the linked list */
  int size;
};

/* a single link in the list */
struct LL_Single_Node {
  /* the node that is next in the list */
  ll_single_node *next;
  /* the value contained in the node */
  ll_single_value value;
};

ll_single new_ll_single () 
{
  /* create a pointer to the linked list */
  ll_single *new_list = (ll_single*) malloc (sizeof (ll_single));
  /* the linked list starts off empty */
  new_list->head = NULL;
  new_list->current = NULL;
  new_list->size = 0;
  return *new_list;
}






#endif