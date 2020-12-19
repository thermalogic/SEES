/*--------------------------------------------- 

    node.cpp

  by Cheng Maohua on 2017-04-06.
-------------------------------------------------------*/

#ifndef NODE_HPP
#define NODE_HPP
#define NULL_VALUE -100.0

#include <string>
#include <unordered_map>
#include <any>
#include <exception> 
#include "CoolPropLib.h"

using namespace std;

typedef unordered_map<string, any>  dictNode;

class Node
{
  public:
    // fields
    string desc;
    int id;
  
    double p;
    double t;
    double h;
    double s;
    double x;
    double mdot;
    bool stateok;
    
    // methods
    Node(dictNode curdictnode);
    ~Node();
    
    void tx();
   
   
};

#endif /* node_hpp */
