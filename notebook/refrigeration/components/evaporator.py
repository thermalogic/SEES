

"""
The Object-oriented Programming Demo of VCR Cycle
    Evaporator: Isobaric heat addition 
"""
from .node import *

class  Evaporator:

    energy = "RefrigerationCapacity"
    devtype = "EVAPORATOR"

    def __init__(self, dictDev, nodes):
        """ Initializes the Evaporator """
        self.name = dictDev['name']
        self.iNode = nodes[dictDev['iNode']]
        self.oNode = nodes[dictDev['oNode']]

    def state(self):
        """ 
            Isobaric heat addition 
        """   
        self.iNode.p=self.oNode.p

    def balance(self):
        """ mass and energy balance  """
        if self.iNode.mdot is not None:
            self.oNode.mdot = self.iNode.mdot
        elif self.oNode.fdot is not None:
            self.iNode.mdot = self.oNode.mdot
        self.Qlow= self.iNode.mdot * (self.oNode.h - self.iNode.h)
 
    def __str__(self):
        result = '\n' + self.name
        result += '\n' + Node.title
        result += '\n' + self.iNode.__str__()
        result += '\n' + self.oNode.__str__()
        result += '\nQlow(kW): \t{:>.2f}'.format(self.Qlow)    
       
        return result
