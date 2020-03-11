#include <iostream>
#include "matplotlibcpp.h"

using namespace std;
namespace plt = matplotlibcpp;

int main() {
    vector<int> x{1,2,3,4};
    vector<int> y{1,7,3,5};
    plt::plot(x,y);
    plt::show();
}
