#include "dll.h"
#include <stdio.h>

int main () 
{
  dll my_dll = dll_new ();
  dll_push (&my_dll, 10);
  dll_push (&my_dll, 30);
  printf ("my_dll.length = %d\n", dll_length (&my_dll));
  return 0;
}