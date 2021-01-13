/*
 The vapor-compression refrigeration cycle simulator for education in C++
*/
#include "vcclib.hpp"

vector<dictDevice> dictNodes = {
    {{"desc", "Evaporator->Compressor"},
     {"id", 1},
     {"p", NAN},
     {"t", 0.0},
     {"x", 1.0},
     {"mdot", 0.08}},
    {{"desc", "Compressor->Condenser"},
     {"id", 2},
     {"p", 0.6854},
     {"t", NAN},
     {"x", NAN},
     {"mdot", NAN}},
    {{"desc", "Condenser->ExpansionValve"},
     {"id", 3},
     {"p", NAN},
     {"t", 26.0},
     {"x", 0.0},
     {"mdot", NAN}},
    {{"desc", "ExpansionValve->Evaporator"},
     {"id", 4},
     {"p", NAN},
     {"t", NAN},
     {"x", NAN},
     {"mdot", NAN}}

};

vector<dictDevice> dictcomps = {{{"name", "Compressor"},
                                 {"classstr", "Compressor"},
                                 {"iNode", 1},
                                 {"oNode", 2}},
                                {{"name", "Condenser"},
                                 {"classstr", "Condenser"},
                                 {"iNode", 2},
                                 {"oNode", 3}},
                                {{"name", "ExpansionValve"},
                                 {"classstr", "ExpansionValve"},
                                 {"iNode", 3},
                                 {"oNode", 4}},
                                {{"name", "Evaporator"},
                                 {"classstr", "Evaporator"},
                                 {"iNode", 4},
                                 {"oNode", 1}}};

int main()
{
  unique_ptr<VCCycle> curcycle(new VCCycle(dictNodes, dictcomps));
  curcycle->state();
  curcycle->balance();
  curcycle->outresults();
  return 0;
}