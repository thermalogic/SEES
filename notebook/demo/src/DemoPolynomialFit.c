/*
   The Demo of Simple PolynomialFit 
*/
#include <stdio.h>


void PolynomialFit(double x[], double y[], int size, int n, double a[]);

int main()
{
    int N = 11;
    double x[11] = {10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0};
    double y[11] = {8.04, 6.95, 7.68, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68};
    int n = 1; // n is the degree of Polynomial
    double a[n + 1];
    int size = sizeof(x) / sizeof(double);
    PolynomialFit(x, y, size, n, a);
    printf("\nThe values of the coefficients are as follows:\n");
    for (int i = 0; i <= n; i++)
        printf("x^ %d = %.4f\n", i, a[i]);
    printf("\nHence the fitted Polynomial is given by:\ny=");
    for (int i = 0; i <= n; i++)
        printf("+( %.4f ) x^ %d", a[i], i);
    printf("\n");
    return 0;
}
