/*
The vapor-compression refrigeration cycle simulator for education in C++
  VCCLIB.hpp for the libvcc
*/
#ifndef VCCLIB_HPP
#define VCCLIB_HPP

#include <string>
#include <unordered_map>
#include <any>
#include <vector>
#include <cmath>
#include <memory>

using namespace std;

typedef unordered_map<string, any> dictDevice;

class VCCycle
{
public:
    // methods
    VCCycle(vector<dictDevice> dictNodes, vector<dictDevice> dictcomps);
    void state();
    void balance();
    void outresults();
};

#endif /* VCCLIB_HPP */
