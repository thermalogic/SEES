
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include "matplotlibcpp.h"

using namespace std;

namespace plt = matplotlibcpp;

// Unit9-2-ctypes:Polynomial Regression
void PolynomialFit(double x[], double y[], int size, int n, double a[]);

int main(void)
{
  vector<double> vecforces;  
  vector<double> vecdistances; 
    
  ifstream fin("../data/springData.csv");
  if(!fin) {
     cerr<<"failed to open file for reading"<<endl;
     return 1;
  }
  string line;
  getline(fin, line);
  while(getline(fin, line))
  {
      istringstream sin(line);
      vector<string> fields; 
      string field;
      while (getline(sin, field, ','))
         fields.push_back(field); 
      string d =fields[0];
      string m =fields[1];
      vecdistances.push_back(atof(d.c_str()));
      vecforces.push_back(9.81*atof(m.c_str()));
  };
    
  fin.close();
 
  int n = 1; // n is the degree of Polynomial
  double a[n + 1];
  int size=vecdistances.size();
  int baddata=6;
  PolynomialFit(vecforces.data(),vecdistances.data(),size - baddata, n, a); 
  cout << "PolynomialFit:k =" << 1 / a[1] << std::endl;
  
  plt::plot(vecforces, vecdistances, "r*");
 
  vector<double> vecpredictedDistances;
  vector<double> vecprevarforces= vector<double>(vecforces.begin(), vecforces.end()-baddata);
  for (auto val : vecprevarforces)
      vecpredictedDistances.push_back(a[1]*val + a[0]);
  plt::plot(vecprevarforces, vecpredictedDistances,"b+");
  plt::plot(vecprevarforces, vecpredictedDistances);
    
  plt::title("Spring Data");
  plt::show();
}
