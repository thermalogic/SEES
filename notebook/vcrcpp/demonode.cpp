/*

g++  -std=c++17 -o ./bin/demonode.exe  -DCOOLPROP_LIB demonode.cpp ./src/node.cpp -I./include -L./bin -lCoolProp

./bin/demonode

*/
#include <string>
#include <iostream>
#include <iomanip>
#include <unordered_map>
#include <any>
#include <vector>
#include "node.hpp"

using namespace std;

int main()
{
  dictNode dictnode1 = {{"desc", "Evaporator to Compressor"},
                        {"id", 1},
                        {"p", NAN},
                        {"t", 0.0},
                        {"x", 0.0},
                        {"mdot", 0.08}};

  Node *curnode1;
  curnode1 = new Node(dictnode1);
  cout << setiosflags(ios::fixed); 
  cout << curnode1->desc << endl;
  cout << curnode1->id << endl;
  cout << curnode1->p << endl;
  cout << curnode1->t << endl;
  cout << curnode1->h << endl;
  cout << curnode1->s << endl;
  cout << curnode1->mdot << endl;

  vector<dictNode> dictNodes = {
      {{"desc", "Evaporator to Compressor"},
       {"id", 1},
       {"p", NAN},
       {"t", 0.0},
       {"x", 0.0},
       {"mdot", 0.08}},
      {{"desc", "Compressor to Condenser"},
       {"id", 2},
       {"p", NAN},
       {"t", NAN},
       {"x", NAN},
       {"mdot", NAN}}};

  vector<Node *> curnodes;
  for (auto &item : dictNodes)
  {
    curnode1 = new Node(item);
    curnodes.push_back(curnode1);
  }

  for (auto &item : curnodes)
  {
    cout << item->desc << endl;
    cout << item->id << endl;
    cout << item->p << endl;
    cout << item->t << endl;
    cout << item->h << endl;
    cout << item->s << endl;
    cout << item->mdot << endl;
  }
  return 0;
}