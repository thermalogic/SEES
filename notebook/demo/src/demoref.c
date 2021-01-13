
/*  
gcc -o demoref demoref.c
*/
#include <stdio.h>
int main()
{
  int a;
  a = 5;
  printf ("The value of a is %d\n", a);
  printf ("The address of a is %d\n", &a);
  
  // ptr_int:the pointer of a  integer variable
  int *ptr_int;
  ptr_int = &a;
  printf ("The value of  ptr_int is %d\n", ptr_int);
  printf ("\tIt stores the value %d\n", *ptr_int);
  
  *ptr_int = 6;
  printf ("It stores the value %d\n", *ptr_int);
  printf ("The new value of a is %d\n", a);
  return 0;
}
