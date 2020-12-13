
"""
The Object-oriented Programming Demo of VCR Cycle
  
  Condenser:Constant pressure heat rejection
"""
from .node import *
import CoolProp.CoolProp as cp

class Condenser:

    energy = "None"
    devtype = "CONDENSER"

    def __init__(self, dictDev, nodes):
        """ Initializes the condenser """
        self.name = dictDev['name']
        self.iNode = nodes[dictDev['iNode']]
        self.oNode = nodes[dictDev['oNode']]

    def state(self):
        """ 
         Constant pressure heat rejection
        """
        self.iNode.p=self.oNode.p
        
    def balance(self):
        """ mass and energy balance of the condenser  """
        if self.iNode.mdot is not None:
            self.oNode.mdot = self.iNode.mdot
        elif self.oNode.fdot is not None:
            self.iNode.mdot = self.oNode.mdot

  
    def __str__(self):
        result = '\n' + self.name
        result += '\n' + Node.title
        result += '\n' + self.iNode.__str__()
        result += '\n' + self.oNode.__str__()
        return result

