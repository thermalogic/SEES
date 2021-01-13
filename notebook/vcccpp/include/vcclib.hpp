/*
The vapor-compression refrigeration cycle simulator for education in C++
  VCCLIB.hpp for the libvcc
*/
#ifndef VCCLIB_HPP
#define VCCLIB_HPP

#include <string>
#include <unordered_map>
#include <map>
#include <any>
#include <vector>
#include <cmath>
#include <memory>

using namespace std;

class Node;

class CompBase;

typedef unordered_map<string, any> dictDevice;
typedef map<int, Node *> mapNode;
typedef unordered_map<string, CompBase *> mapComponent;

class VCCycle
{
public:
    mapNode nodes;
    mapComponent comps;

    double Wc;
    double Qin;
    double cop;

    // methods
    VCCycle(vector<dictDevice> dictNodes, vector<dictDevice> dictcomps);
   
    void state();
    void balance();
    void outresults();
};

#endif /* VCCLIB_HPP */
