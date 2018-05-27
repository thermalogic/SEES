
/* Example to demonstrate use of reference operator in C programming. 
gcc -o demoref.c
*/
#include <stdio.h>
int main()
{
  int var = 5;
  printf("Value: %d\n", var);
  printf("Address: %u\n", &var);  //reference operator, Notice, the & before var.
  printf("Value: %d\n", *(&var));  // dereference operator,Notice, the * before ＆var.  
  return 0;
}