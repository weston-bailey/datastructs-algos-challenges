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
ll_single ll_single_pop (ll_single *list);
ll_single ll_single_prepend (ll_single *list, ll_single_value value);
ll_single ll_single_unshift (ll_single *list);
ll_single ll_single_splice (ll_single *list, int index);

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

/* there is a bug if you pop off a list until it is empty */
ll_single ll_single_pop (ll_single *list)
{
  /* return early if the list is empty */
  if (!list->head) return *list;
  /* zip to the end and keep track if the previous node*/
  ll_single_node *prev;
  list->current = list->head;
  while (list->current->next) {
    prev = list->current;
    list->current = list->current->next;
  }
  /* clean up and dcrement size */
  prev->next = NULL;
  free (list->current);
  list->current = NULL;
  list->size--;
  if (list->size == -1) list->head = NULL;

  return *list;
}

ll_single ll_single_prepend (ll_single *list, ll_single_value value)
{
  /* create a new node */
  ll_single_node *new_node = (ll_single_node*) malloc (sizeof (ll_single_node));
  new_node->value = value;
  /* set the head to be the new node's next */
  new_node->next = list->head;

  /* set the new node to be the head, inc the size */
  list->head = new_node;
  list->size++;
  return *list;
}

ll_single ll_single_unshift (ll_single *list)
{
  /* store a reference to the head */
  ll_single_node *head;
  head = list->head;

  /* set the head's next to be the head */
  list->head = head->next;

  /* free the head and clean up, dec the size */
  free (head);
  list->size--;

  return *list;
}

ll_single ll_single_splice (ll_single *list, int index)
{
  if (index > list->size) return *list;
  /* loop to index, keeping track prev */
  int i;
  ll_single_node *prev;
  list->current = list->head;
  while (i < index) {
    prev = list->current;
    list->current = list->current->next;
    i++;
  }
  /* link the prev to the current's next */
  prev->next = list->current->next;
  /* clean up and dec the list size */
  free (list->current);
  list->current = NULL;
  list->size--;

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
    printf("list is empty\n");
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