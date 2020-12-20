/*
 
nodes is dict: map<int, Node *> mapNode
  
g++  -std=c++17 -o ./bin/demonode.exe  -DCOOLPROP_LIB demonode.cpp ./src/node.cpp -I./include -L./bin -lCoolProp

./bin/demonode

*/
#include <string>
#include <iostream>
#include <iomanip>
#include<map>
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

    typedef map<int, Node *> mapNode;
    mapNode dNodes;
    for (auto &item : dictNodes)
    {
        int id=any_cast<int>(item["id"]);
        dNodes.insert(mapNode::value_type(id,new Node(item)));
    }
    mapNode::iterator iter;
    for(iter=dNodes.begin(); iter != dNodes.end(); iter++)  
    {  
        cout<<iter->first<<"\t"<<iter->second->id<<"\t"<<iter->second->desc<<endl;  
    };  

    if((iter=dNodes.find(1))!=dNodes.end()) 
		cout<<"get it,value= "<<iter->second->id<<"\t"<<iter->second->desc<<endl;
	else
		cout<<"not find"<<endl;
    return 0;
}