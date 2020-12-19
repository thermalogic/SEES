/*

g++  -std=c++17 -o ./bin/demonode.exe  -DCOOLPROP_LIB demonode.cpp ./src/node.cpp -I./include -L./bin -lCoolProp

./bin/demonode

*/
#include <string>
#include <iostream>
#include <unordered_map>
#include <any>
#include <iomanip>
#include <vector>
#include "node.hpp"

using namespace std;

int main()
{
    dictNode dictnode1 = {{"desc", "Compress to Condenser"},
                          {"id", 1},
                          {"p", NULL_VALUE},
                          {"t", 0.0},
                          {"x", 0.0},
                          {"mdot", 0.08}};

    Node *curnode1;
    curnode1 = new Node(dictnode1);
    cout << std::setiosflags(std::ios::fixed) << curnode1->desc << endl;
    cout << std::setiosflags(std::ios::fixed) << curnode1->id << endl;
    cout << std::setiosflags(std::ios::fixed) << curnode1->p << endl;
    cout << std::setiosflags(std::ios::fixed) << curnode1->t << endl;
    cout << std::setiosflags(std::ios::fixed) << curnode1->h << endl;
    cout << std::setiosflags(std::ios::fixed) << curnode1->s << endl;
    cout << std::setiosflags(std::ios::fixed) << curnode1->mdot << endl;

   vector<dictNode> dictNodes={
                    {{"desc", "Compress to Condenser"},
                    {"id", 1},
                    {"p", NULL_VALUE},
                    {"t", 0.0},
                     {"x",0.0},
                     {"mdot",0.08}},
                     {{"desc", "Compressor to Condenser"},
                    {"id", 2},
                    {"p", NULL_VALUE},
                    {"t", NULL_VALUE},
                     {"x",NULL_VALUE},
                     {"mdot", NULL_VALUE}}
                     };

    vector<Node*> curnodes;
    for (auto &item : dictNodes)
    {
         curnode1 = new Node(item);
         curnodes.push_back(curnode1);
    }
    
    for (auto &item : curnodes)
    { cout << std::setiosflags(std::ios::fixed) << item->desc << endl;
      cout << std::setiosflags(std::ios::fixed) << item->id << endl;
      cout << std::setiosflags(std::ios::fixed) << item->p << endl;
      cout << std::setiosflags(std::ios::fixed) << item->t << endl;
       cout << std::setiosflags(std::ios::fixed) << item->h << endl;
       cout << std::setiosflags(std::ios::fixed) << item->s << endl;
      cout << std::setiosflags(std::ios::fixed) << item->mdot << endl;
    }
    return 0;

}