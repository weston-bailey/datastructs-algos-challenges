#ifndef LL_SINGLE
#define LL_SINGLE
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>


typedef struct LL_Single ll_single;
typedef struct LL_Single_Node ll_single_node;
typedef int ll_single_value;

ll_single ll_single_new ();
ll_single ll_single_push (ll_single *list, ll_single_value value);

void ll_single_print (ll_single *list);
int ll_single_length (ll_single list);

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

ll_single ll_single_new () 
{
  /* create a pointer to the linked list */
  ll_single *new_list = (ll_single*) malloc (sizeof (ll_single));

  /* the linked list starts off empty */
  new_list->head = NULL;
  new_list->current = NULL;
  new_list->size = -1;
  return *new_list;
}

ll_single ll_single_push (ll_single *list, ll_single_value value) 
{
  /* create the new node and value to sotre in it */
  ll_single_node *new_node = (ll_single_node*) malloc (sizeof (ll_single_node));
  ll_single_value *new_value = (ll_single_value*) malloc (sizeof (ll_single_value));

  /* set up the new node */
  new_node->value = *new_value = value;
  new_node->next = NULL;

  /* if the list has head, we need to zip to the end and add the new node */
  if (list->head) {
    /* set the current to be the haed to start */
    list->current = list->head;
    /* loop until there is a NULL value in the current node's head */
    while (list->current->next) {
      /* the current to to be the next to keep looping */
      list->current = list->current->next;
    } 
    /* once its at the end, set to next to be the new node */
    list->current->next = new_node;
  } else {
    /* the the case this is the first thing added to the list */
    list->head = new_node;
  }

  /* increment the count in either case */
  list->size++;
  
  return *list;
}

/* returns the length of the linked list */
int ll_single_length (ll_single list) 
{
  return list.size;
}
/* prints every value in the list */
void ll_single_print (ll_single *list)
{
  if (list->size == -1) {
    printf("list is empty");
    return;
  } 

  list->current = list->head;
  int i = 0;
  while (list->current) {
    printf("[%d] = %d\n", i, list->current->value);
    list->current = list->current->next;
    i++;
  }

}


#endif