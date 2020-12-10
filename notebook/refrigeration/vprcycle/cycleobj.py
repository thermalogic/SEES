"""
 General Object-oriented Abstraction of vpr Cycle 

RefrigerationCycle: the Simulator class of VPR Cycle  

dictcycle={"name":namestring,
                     "nodes":[{node1},{node2},...],
                     "comps":[{component1},{component2},...]
                     }
  
Author:Cheng Maohua  Email: cmh@seu.edu.cn

"""

import time

from components.node import Node
from components import compdict


class RefrigerationCycle:

    def __init__(self, dictcycle):
        """
          dictcycle={"name":namestring,
                     "nodes":[{node1},{node2},...],
                     "comps":[{component1},{component2},...]
                     }
          TO:           
             self.nodes : dict of all node objects
             self.comps : dict of all component objects
        """
        self.name = dictcycle["name"]
        dictnodes = dictcycle["nodes"]
        dictcomps = dictcycle["comps"]

        # 1 convert dict to the object of nodes
        self.NodeNum = len(dictnodes)
        self.nodes = {}
        for curnode in dictnodes:
            self.nodes[curnode["id"]] = Node(curnode)

        # 2 convert dict to the object of Comps
        self.DevNum = len(dictcomps)
        self.comps = {}
        for curdev in dictcomps:
            self.comps[curdev['name']] = compdict[curdev['devtype']](
                curdev, self.nodes)
       
        self.Wc = 0
        self.Qlow = 0
        self.cop = 0.0

       
    def ComponentState(self):
        for key in self.comps:
            self.comps[key].state()
       
        for key in self.nodes:
            if self.nodes[key].stateok==False:
              self.nodes[key].setstate()

    def ComponentBalance(self):
        for curdev in self.comps:
            self.comps[curdev].balance()
    
    def simulator(self):
        self.ComponentState()
        self.ComponentBalance()

        self.Wc= 0
        self.Qlow = 0

        for key in self.comps:
            if self.comps[key].energy == "CompressionWork":
                self.Wc += self.comps[key].Wc
            elif self.comps[key].energy == "RefrigerationCapacity":
                self.Qlow += self.comps[key].Qlow

        self.cop = self.Qlow / self.Wc
        self.Qlow += self.Qlow*60*(1/211)

    def __setformatstr(self, formatstr, result):
        result += formatstr.format('CompressionWork(kW)', self.Wc)
        result += formatstr.format('RefrigerationCapacity(ton)', self.Qlow)
        result += formatstr.format('cop', self.cop)
        return result

    def __str__(self):
        str_curtime = time.strftime(
            "%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
        result = "\n Rankine Cycle: {}, Time: {}\n".format(
            self.name, str_curtime)
        try:
            formatstr = "{:>20} {:>.2f}\n"
            result = self.__setformatstr(formatstr, result)
        except:
            formatstr = "{} {}\n"
            result = self.__setformatstr(formatstr, result)
        return result
