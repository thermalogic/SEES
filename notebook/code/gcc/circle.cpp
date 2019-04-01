
#include <iostream>
#include <math.h>
using namespace std;

class TCircle
// A Circle instance models a circle with a radius 
{
  private:
    float radius;
  
  public: 
    float area;
    
    TCircle();
    TCircle(float fradius);
    ~ TCircle();
    
    void cal_area();
};

TCircle:: TCircle()
{
  radius=1.0;   
};

TCircle:: TCircle(float fradius)
{
  radius=fradius;   
};

TCircle::~ TCircle()
{
    
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
   cout << "The Circle: radius="<<radius<<"\tarea="<<c1.area<<endl;
   return 0;
}
