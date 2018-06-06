/*
gcc -o demostdio demostdio.c
*/
#include <stdio.h>

int main ()
{
  char name[80];
  int age;
  float num;  

  printf ("Enter your family name: ");
  scanf ("%79s",name);  
  
  printf ("Enter your age: ");
  scanf ("%d",&age);
  printf ("Mr. %s , %d years old.\n",name,age);
    
  printf("Enter a number: ");
  scanf("%f", &num);  
  printf ("You have entered %f\n",num); 
    
  return 0;
}