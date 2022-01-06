
#include <iostream>
#include <math.h>
using namespace std;

class Circle // name
{
private:
   float radius; // attributes(variables)
public:
   Circle(float r = 1.0);  // methods
   float getRadius();
   float getArea(); 
};

Circle::Circle(float r)
{
   radius = r;
};

float Circle::getRadius()
{
   return radius;
};

float Circle::getArea()
{
   return radius * radius * M_PI;
};

int main()
{
   float radius = 2.1;
   Circle c1(radius);
   cout << "The Circle: radius=" << c1.getRadius() << "\tarea=" <<c1.getArea() << endl;
   return 0;
}
