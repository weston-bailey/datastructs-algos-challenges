#ifndef _DLL_
#define _DLL_
#include <stddef.h>
#include <stdlib.h>

typedef struct DLL dll;
typedef struct DLL_Node dll_node;
typedef int dll_value;

dll dll_new ();
dll dll_push (dll *list, dll_value value);
dll dll_pop (dll *list);
dll dll_prepend (dll *list, dll_value value);
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

dll dll_push (dll *list, dll_value *value) 
{
  return *list; 
}

dll dll_pop (dll *list) {
  return *list;
}

dll dll_prepend (dll *list, dll_value value) 
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