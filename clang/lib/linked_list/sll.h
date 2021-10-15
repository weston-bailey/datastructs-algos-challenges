#ifndef _SLL_
#define _SLL_
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>


typedef struct SLL sll;
typedef struct SLL_Node sll_node;
typedef int sll_value;

sll sll_new ();
sll sll_push (sll *list, sll_value value);
sll sll_pop (sll *list);
sll sll_prepend (sll *list, sll_value value);
sll sll_unshift (sll *list);
sll sll_splice (sll *list, int start_index, int end_index);

void sll_print (sll *list);
int sll_length (sll list);

/* linked list manager struct */
struct SLL {
  /* the first node in the head of the liked list */
  sll_node *head;
  /* the node that is currently being checked */
  sll_node *current;
  /* the number of nodes in the linked list */
  int size;
};

/* a single link in the list */
struct SLL_Node {
  /* the node that is next in the list */
  sll_node *next;
  /* the value contained in the node */
  sll_value value;
};

sll sll_new () 
{
  /* create a pointer to the linked list */
  sll *new_list = (sll*) malloc (sizeof (sll));

  /* the linked list starts off empty */
  new_list->head = NULL;
  new_list->current = NULL;
  new_list->size = -1;
  return *new_list;
}

sll sll_push (sll *list, sll_value value) 
{
  /* create the new node and value to sotre in it */
  sll_node *new_node = (sll_node*) malloc (sizeof (sll_node));
  sll_value *new_value = (sll_value*) malloc (sizeof (sll_value));

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

sll sll_pop (sll *list)
{
  /* return early if the list is empty */
  if (!list->head) return *list;
  /* zip to the end and keep track if the previous node*/
  sll_node *prev;
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

sll sll_prepend (sll *list, sll_value value)
{
  /* create a new node */
  sll_node *new_node = (sll_node*) malloc (sizeof (sll_node));
  new_node->value = value;
  /* set the head to be the new node's next */
  new_node->next = list->head;

  /* set the new node to be the head, inc the size */
  list->head = new_node;
  list->size++;
  return *list;
}

sll sll_unshift (sll *list)
{
  /* store a reference to the head */
  sll_node *head;
  head = list->head;

  /* set the head's next to be the head */
  list->head = head->next;

  /* free the head and clean up, dec the size */
  free (head);
  list->size--;
  if (list->size == -1) list->head = NULL;

  return *list;
}

sll sll_splice (sll *list, int start_index, int end_index)
{
  /* return early if start_index or end_index is out of bounds */
  if (start_index > list->size) return *list;
  /* remove until the end of the list if th end_index is out of bounds */
  if(start_index + end_index > list->size) end_index =list->size - start_index;


  /* loop to start_index, keeping track prev */
  int i = 0;
  sll_node* prev;
  list->current = list->head;
  while (i < start_index) {
    prev = list->current;
    list->current = list->current->next;
    i++;
  }
  /* make an array to hold all the nodes to remove -- add from start_index to end_index */
  sll_node* nodes[end_index];
  i = 0;
  while (i < end_index) {
    nodes[i] = list->current;
    list->current = list->current->next;
    i++;
  }

  /* link the prev to the current's next */
  prev->next = list->current->next;
  /* clean up and dec the list size */
  size_t nodes_size = sizeof (nodes) / sizeof (sll_node*);
  for (i = 0; i < nodes_size; i++) {
    free (nodes[i]);
  }
  list->current = NULL;
  list->size -= (int)nodes_size;

  return *list;
}


/* returns the length of the linked list */
int sll_length (sll list) 
{
  return list.size;
}

/* prints every value in the list */
void sll_print (sll *list)
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