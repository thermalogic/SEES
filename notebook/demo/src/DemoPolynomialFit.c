/*
   The Demo of Simple PolynomialFit 
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void PolynomialFit(double x[], double y[], int size, int n, double a[]);

int main()
{

  int size = 19;
  double distances[size];
  double masses[size];
  double forces[size];

   FILE *fp = fopen("./demo/data/springData.csv", "r");
  if(fp == NULL) {
     fprintf(stderr, "failed to open file for reading\n");
     return 1;
  }
  
  char line[1024];
  int i=0;
  while(fgets(line, sizeof(line), fp))
  {
    char *save_ptr;
    char *d = strtok_r(line, ",", &save_ptr);
    if (d == NULL) {
       break;
    }
     char *m = strtok_r(NULL, ",", &save_ptr);
     if (atof(d) > 0)
           distances[i-1] = atof(d);
     if (atof(m) > 0)
           masses[i-1] = atof(m);
    i++;  
  }
  for (int n = 0; n < size; n++)
  {
    forces[n] = masses[n] * 9.81;
  }
  int n = 1; // n is the degree of Polynomial
  double a[n + 1];
  PolynomialFit(forces, distances, size - 6, n, a);
  printf(" PolynomialFit: k = %.2f", 1 / a[1]);
  return 0;
}   
