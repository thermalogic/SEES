
#include <iostream>
#include "../include/matplotlibcpp.h"

using namespace std;

namespace plt = matplotlibcpp;

// Unit9-2-ctypes:Polynomial Regression
void PolynomialFit(double x[], double y[], int size, int n, double a[]);

int main(void)
{
  double distances[] = {0.0865, 0.1015, 0.1106, 0.1279, 0.1892,
                        0.2695, 0.2888, 0.2425, 0.3465, 0.3225,
                        0.3764, 0.4263, 0.4562, 0.4502, 0.4499,
                        0.4534, 0.4416, 0.4304, 0.437};
  double masses[] = {0.10, 0.15, 0.20, 0.25, 0.30,
                     0.35, 0.40, 0.45, 0.50, 0.55,
                     0.60, 0.65, 0.70, 0.75, 0.80,
                     0.85, 0.90, 0.95, 1.00};

  int n = 1; // n is the degree of Polynomial
  double a[n + 1];

  int size = (sizeof(masses) / sizeof(double));
  double forces[size];
  for (int i = 0; i < size; i++)
    forces[i] = masses[i] * 9.81;
  PolynomialFit(forces, distances, size - 6, n, a);
  cout << "PolynomialFit:k =" << 1 / a[1] << std::endl;
  //plot
  vector<double> vecforces(forces, forces+sizeof(forces)/sizeof(double)-6);  
  vector<double> vecdistances(distances, distances+sizeof(distances)/sizeof(double)-6); 
  plt::plot(vecforces, vecdistances, "r*");
  
  vector<double> vecpredictedDistances;
  for (int i = 0; i < size-6; i++)
      vecpredictedDistances.push_back(a[1]*forces[i] + a[0]);
  plt::plot(vecforces, vecpredictedDistances,"b+");
  plt::plot(vecforces, vecpredictedDistances);
  
  plt::title("Sample figure");
  plt::show();
}
