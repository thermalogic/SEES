
#include <iostream>

#include "statistics.h"
#include "number.h"

using namespace std;

int main() {
    
     double a[] = {8, 4, 5, 3, 2};
     int len= sizeof(a)/sizeof(*a);
     cout<<"mean is "<<mean(a,  len)<<endl; 
    
     int n =5;
     cout<<"the factorial of "s<<n<<" is "<<factorial(n)<<endl;  // 5!=120
     return 0;
}
