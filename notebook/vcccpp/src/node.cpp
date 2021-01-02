/*----------------------------------------------------

  node.cpp
----------------------------------------------------------*/

#include "node.hpp"

Node::Node(dictNode curdictnode)
{
   desc = any_cast<const char *>(curdictnode["desc"]);
   id = any_cast<int>(curdictnode["id"]);
   try
   {
      p = any_cast<double>(curdictnode["p"]);
   }
   catch (...)
   {
      p = NAN;
   }
   try
   {
      t = any_cast<double>(curdictnode["t"]);
   }
   catch (...)
   {
      t = NAN;
   }
   try
   {
      x = any_cast<double>(curdictnode["x"]);
   }
   catch (...)
   {
      x = NAN;
   }
   try
   {
      mdot = any_cast<double>(curdictnode["mdot"]);
   }
   catch (...)
   {
      mdot = NAN;
   }
   h = NAN;
   s = NAN;
   stateok = false;

   if (!isnan(t) & !isnan(x))
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
      p = PropsSI("P", "T", 273.15 + t, "Q", x, "R134a") / 1.0e6;
      h = PropsSI("H", "T", 273.15 + t, "Q", x, "R134a") / 1000;
      s = PropsSI("S", "T", 273.15 + t, "Q", x, "R134a") / 1000;
      stateok = true;
   }
   catch (exception &e)
   {
      stateok = false;
   }
}
