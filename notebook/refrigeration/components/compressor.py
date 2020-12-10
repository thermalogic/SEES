
from .node import *

class Compressor:
    """ Isentropic compression of the refrigerant"""
    energy = "workRequired"
    devtype = "COMPRESSOR"

    def __init__(self, dictDev, nodes):
        """
        Initializes the pump with the conditions
        """
        self.name = dictDev['name']
        self.iNode = nodes[dictDev['iNode']]
        self.oNode = nodes[dictDev['oNode']]
  
    def state(self):
        """
        Isentropic compression of the refrigeran
        """
        self.oNode.s=self.iNode.s
        self.oNode.ps()

    def balance(self):
        """  mass and energy balance the pump    """
        # mass balance
        if self.iNode.mdot is not None:
            self.oNode.mdot = self.iNode.mdot
        elif self.oNode.mdot is not None:
            self.iNode.mdot = self.oNode.mdot

        # energy
        self.WRequired = self.iNode.mdot * (self.oNode.h - self.iNode.h)

  
    def __str__(self):
        result = '\n' + self.name
        result += '\n' + Node.title
        result += '\n' + self.iNode.__str__()
        result += '\n' + self.oNode.__str__()

        result += '\nWRequired(kW): \t{:>.2f}'.format(self.WRequired)
        return result
