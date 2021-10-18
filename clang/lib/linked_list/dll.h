#ifndef _DLL_
#define _DLL_
#include <stddef.h>
#include <stdlib.h>

typedef struct DLL dll;
typedef struct DLL_Node dll_node;
typedef int dll_value;

dll dll_new ();
dll dll_reset (dll *list);
dll_node dll_node_new ();
dll dll_push (dll *list, dll_value value);
dll dll_pop (dll *list);
dll dll_shift (dll *list, dll_value value);
dll dll_unshift (dll *list);
dll dll_splice (dll *list, int start_index, int end_index);

void dll_print (dll *list);
int dll_length (dll *list);

struct DLL {
  dll_node *head;
  dll_node *tail;   
  dll_node *current;
  int length;
};

struct DLL_Node {
  dll_node *next;
  dll_node *prev;
  dll_value value;
};

/* create a new doubly linked list */
dll dll_new () 
{
  dll *list = (dll*) malloc (sizeof (dll));

  list->head = NULL;
  list->tail = NULL;
  list->current = NULL;
  list->length = -1;

  return *list; 
}

/* resets a dll (useful when list is emptied and memory is freed) */
dll dll_reset (dll *list) 
{
  list->head = NULL;
  list->tail = NULL;
  list->current = NULL;
  list->length = -1;

  return *list; 
}


/* creates a new double linked list node */
dll_node dll_node_new ()
{
  dll_node *new_node = (dll_node*) malloc (sizeof (dll_node));
  new_node->next = NULL;
  new_node->next = NULL;
  new_node->next = NULL;

  return *new_node;
} 
/* add value to the end of the list */
dll dll_push (dll *list, dll_value value) 
{
  /* create a new node for the list and inc the len */
  dll_node *new_node = new_node_new ();
  new_node->value = value;
  list->length++;

  /* if this is the fitst node in the list */
  if (!list->tail) {
    list->head = new_node;
    list->tail = new_node;

    return *list;
  }

  /* add node to the end of the list */
  list->tail->next = new_node;

  return *list;
}

/* remove the last node on in the list */
dll dll_pop (dll *list) {  
  /* just return if the list is empty */
  if (!list->tail) return *list;
  /* in this case, there is only one item in the list */
  if (!list->tail->prev) {
    free (list->tail);
    return dll_reset (&list);
  }
  return *list;
}

dll dll_shift (dll *list, dll_value value) 
{
  return *list;
}

dll dll_unshift (dll *list) 
{
  return *list;
}

dll dll_splice (dll *list, int start_index, int end_index) 
{
  return *list;
}

void dll_print (dll *list) 
{

}

int dll_length (dll *list) 
{
  return list->length;
}

#endif