/*--------------------------------------------- 

  node.cpp
-------------------------------------------------------*/

#ifndef NODE_HPP
#define NODE_HPP

#include <string>
#include <unordered_map>
#include <any>
#include <exception>
#include <cmath>
#include "CoolPropLib.h"

using namespace std;

typedef unordered_map<string, any> umapNode;

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
  Node(umapNode curdictnode);
  ~Node();

  void tx();
};

#endif /* node_hpp */
