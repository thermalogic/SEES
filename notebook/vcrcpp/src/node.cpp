/*----------------------------------------------------

  node.cpp
----------------------------------------------------------*/

#include "node.hpp"

Node::Node(dictNode curdictnode)
{
    desc =any_cast<const char *>(curdictnode["desc"]);
    id = any_cast<int>(curdictnode["id"]);
    p = any_cast<double>(curdictnode["p"]);
    t = any_cast<double>(curdictnode["t"]);
    x = any_cast<double>(curdictnode["x"]);
    mdot=any_cast<double>(curdictnode["mdot"]);
 
    h=NULL_VALUE;
    s=NULL_VALUE;
    stateok = false;

    if ((t!=NULL_VALUE) && (x!=NULL_VALUE))
    {
       tx();
    }
}

Node::~Node()
{

}

void Node::tx()
{
  try
  {   
       p =PropsSI("P", "T", 273.15+t,"Q",x, "R134a")/1.0e6;
       h = PropsSI("H", "T", 273.15+t, "Q", x, "R134a")/1000;
       s = PropsSI("S", "T", 273.15+t, "Q", x, "R134a")/1000;
       stateok = true;
  }
  catch(exception& e)
  {
     stateok = false;
  }
 }


