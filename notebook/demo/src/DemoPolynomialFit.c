/*
   The Demo of Simple PolynomialFit 
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void PolynomialFit(double x[], double y[], int size, int n, double a[]);

int main()
{

  int MAX_LINE_SIZE = 25;
  char file_name[] = "./data/springData.csv";
  FILE *fp;
  fp = fopen(file_name, "r");

  if (!fp)
  {
    fprintf(stderr, "failed to open file for reading\n");
    return 1;
  }

  char line[MAX_LINE_SIZE];
  char *result = NULL;
  int size = 19;
  double distances[size];
  double masses[size];
  double forces[size];

  int ix = 0;
  int iy = 0;

  while (fgets(line, MAX_LINE_SIZE, fp) != NULL)
  {

    result = strtok(line, ",");
    int i = 0;
    while (result != NULL)
    {
      if (i != 0)
      {
        if (atof(result) > 0)
        {
          masses[ix] = atof(result);
          ix++;
        }
      }
      else
      {
        if (atof(result) > 0)
        {
          distances[iy] = atof(result);
          iy++;
        }
        i++;
      }
      result = strtok(NULL, ",");
    }
  }
  fclose(fp);

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
