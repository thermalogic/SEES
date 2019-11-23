
#include "../include/matplotlibcpp.h"
namespace plt = matplotlibcpp;

int main() {
    std::vector<int> x{1,2,3,4};
    std::vector<double> y{1,7,3,5};
    // plt::plot({1,2,3,4}, {1,7,3,5});
    plt::plot(x,y);
    plt::show();
}
