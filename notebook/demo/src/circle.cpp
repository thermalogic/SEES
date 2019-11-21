
#include <iostream>
#include <math.h>
using namespace std;

class TCircle
// A Circle instance models a circle with a radius 
{
  private:
  
  public: 
    float radius;
    float area;
    
    TCircle(float fradius=1.0);
    
    void cal_area();
};

TCircle:: TCircle(float fradius)
{
    radius=fradius;   
};

void TCircle::cal_area()
{
    area=radius * radius * M_PI;
};        

int main() {
   float radius=2.1;
   float area;
   TCircle c1(radius);
   c1.cal_area(); 
   cout << "The Circle: radius="<<c1.radius<<"\tarea="<<c1.area<<endl;
   return 0;
}
