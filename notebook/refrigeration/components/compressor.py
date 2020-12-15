
"""
The Object-oriented Programming Demo of VCR Cycle
  Compressor : Isentropic compression (ideal VCR cycle)
"""
from .node import *


class Compressor:
    """ Isentropic compression of the refrigerant"""
    energy = "CompressionWork"
    devtype = "COMPRESSOR"

    def __init__(self, dictDev, nodes):
        """
        Initializes 
        """
        self.name = dictDev['name']
        self.iNode = nodes[dictDev['iNode']]
        self.oNode = nodes[dictDev['oNode']]
        self.Wc = None

    def state(self):
        """
        Isentropic compression  (ideal VPR cycle)
        """
        self.oNode.s = self.iNode.s

    def balance(self):
        """  mass and energy balance    """
        # mass balance
        if self.iNode.mdot is not None:
            self.oNode.mdot = self.iNode.mdot
        elif self.oNode.mdot is not None:
            self.iNode.mdot = self.oNode.mdot
        # energy
        self.Wc = self.iNode.mdot * (self.oNode.h - self.iNode.h)

    def __str__(self):
        result = '\n' + self.name
        result += '\n' + Node.title
        result += '\n' + self.iNode.__str__()
        result += '\n' + self.oNode.__str__()
        result += '\nWc(kW): \t{:>.2f}'.format(self.Wc)
        return result
