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
   double forces[size];

   FILE *fp = fopen("./demo/data/springData.csv", "r");
   if (fp == NULL)
   {
      fprintf(stderr, "failed to open file for reading\n");
      return 1;
   }

   char line[1024];
   fgets(line, sizeof(line), fp);
   int i = 0;
   while (fgets(line, sizeof(line), fp))
   {
      char *save_ptr;
      // The first call to strtok_r(), str point to the string to be parsed" line
      char *d = strtok_r(line, ",", &save_ptr);
      // In subsequent calls, str is NULL, and saveptr is unchanged since the previous call.
      char *m = strtok_r(NULL, ",", &save_ptr);
      distances[i] = atof(d);
      forces[i] = atof(m) * 9.81;
      i++;
   };
   fclose(fp);

   int n = 1; // n is the degree of Polynomial
   double a[n + 1];
   PolynomialFit(forces, distances, size - 6, n, a);
   printf(" PolynomialFit: k = %.6f", 1 / a[1]);
   return 0;
}
