"""
The  Object-oriented Programming Demo  of VCR Cycle

VCRCycle: the Simulator class of VCR Cycle 

dictcycle={"name":namestring,
                     "nodes":[{node1},{node2},...],
                     "comps":[{component1},{component2},...]
                     }
"""

import time

from components.node import Node
from components import compdict


class VCRCycle:

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

    def ComponentState(self):
        for key in self.comps:
            self.comps[key].state()

        for key in self.nodes:
            if self.nodes[key].stateok == False:
                self.nodes[key].setstate()

    def ComponentBalance(self):
        for curdev in self.comps:
            self.comps[curdev].balance()

    def simulator(self):
        self.ComponentState()
        self.ComponentBalance()

        self.Wc = 0
        self.Qlow = 0

        for key in self.comps:
            if self.comps[key].energy == "CompressionWork":
                self.Wc += self.comps[key].Wc
            elif self.comps[key].energy == "RefrigerationCapacity":
                self.Qlow += self.comps[key].Qlow

        self.cop = self.Qlow / self.Wc
        self.Qlow = self.Qlow*60*(1/211)

    def __setformatstr(self, formatstr, result):
        result += formatstr.format('Compression Work(kW): ', self.Wc)
        result += formatstr.format('Refrigeration Capacity(ton): ', self.Qlow)
        result += formatstr.format('The coefficient of performance: ', self.cop)
        return result

    def __str__(self):
        str_curtime = time.strftime(
            "%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
        result = "\nRefrigeration Cycle: {} (Time: {})\n".format(
            self.name, str_curtime)
        try:
            formatstr = "{:>35} {:>5.2f}\n"
            result = self.__setformatstr(formatstr, result)
        except:
            formatstr = "{} {}\n"
            result = self.__setformatstr(formatstr, result)
        return result
