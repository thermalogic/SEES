/*
 
nodes is dict: map<int, Node *> mapNode
  
g++  -std=c++17 -o ./bin/demonode.exe  -DCOOLPROP_LIB demonode.cpp ./src/node.cpp -I./include -L./bin -lCoolProp

./bin/demonode

*/
#include <string>
#include <iostream>
#include <iomanip>
#include <map>
#include <any>
#include <vector>
#include "node.hpp"

using namespace std;

int main()
{
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

    typedef map<int, Node *> mapNode;
    mapNode dNodes;
    for (auto &item : dictNodes)
    {
        int id = any_cast<int>(item["id"]);
        dNodes.insert(mapNode::value_type(id, new Node(item)));
    }

    cout << setiosflags(ios::fixed);
    for (mapNode::iterator iter = dNodes.begin(); iter != dNodes.end(); iter++)
    {
        cout << iter->first << "\t" << iter->second->id << "\t" << iter->second->desc;
        cout << "\t" << iter->second->p << "\t" << iter->second->t << "\t" << iter->second->h << "\t" << iter->second->s <<  "\t"<<iter->second->x << endl;
    };

    for (auto &item : dictNodes)
    {
        int i = any_cast<int>(item["id"]);
        cout << i << "\t" << dNodes[i]->id << "\t" << dNodes[i]->desc;
        cout << "\t" << dNodes[i]->p << "\t" << dNodes[i]->t << "\t" << dNodes[i]->h << "\t" << dNodes[i]->s << "\t" << dNodes[i]->x << endl;
    }


    for (mapNode::iterator iter = dNodes.begin(); iter!= dNodes.end(); iter++)
        delete iter->second;
    dNodes.clear();

    return 0;
}