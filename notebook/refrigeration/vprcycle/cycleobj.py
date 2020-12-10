"""
 General Object-oriented Abstraction of vpr Cycle 

RefrigerationCycle: the Simulator class of Rankine Cycle  

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

        self.totalworkRequired = 0
        self.totalheatAdded = 0
        self.cop = 0.0

       
    def ComponentState(self):
        for key in self.comps:
            self.comps[key].state()

    def ComponentBalance(self):
        keys = list(self.comps.keys())
        deviceok = False

        i = 0  # i: the count of deviceok to avoid endless loop
        while (deviceok == False and i <= self.DevNum):

            for curdev in keys:
                try:
                    self.comps[curdev].balance()
                    keys.remove(curdev)
                except:
                    pass

            i += 1
            if (len(keys) == 0):
                deviceok = True

        # for debug: check the failed devices
        if (len(keys) > 0):
            print(keys)

    def simulator(self):
        self.ComponentState()
        self.ComponentBalance()

        self.totalworkRequired = 0
        self.totalheatAdded = 0

        for key in self.comps:
            if self.comps[key].energy == "workRequired":
                self.totalworkRequired += self.comps[key].workRequired
            elif self.comps[key].energy == "heatAdded":
                self.totalheatAdded += self.comps[key].heatAdded

        self.cop = self.HeatRate / self.totalheatAdded

  
    def __setformatstr(self, formatstr, result):
        result += formatstr.format('totalWRequired(MW)', self.totalWRequired)
        result += formatstr.format('totalQAdded(MW)', self.totalQAdded)
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
