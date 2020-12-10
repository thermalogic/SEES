
from .node import *


class Condenser:

    energy = "heatExtracted"
    devtype = "CONDENSER"

    def __init__(self, dictDev, nodes):
        """ Initializes the condenser """
        self.name = dictDev['name']
        self.iNode = nodes[dictDev['iNode']]
        self.oNode = nodes[dictDev['oNode']]

    def state(self):
        pass

    def balance(self):
        """ mass and energy balance of the condenser  """
        if self.iNode.mdot is not None:
            self.oNode.mdot = self.iNode.mdot
        elif self.oNode.fdot is not None:
            self.iNode.mdot = self.oNode.mdot

        self.QExtracted = self.iNode.mdot * (self.iNode.h - self.oNode.h)

    def __str__(self):
        result = '\n' + self.name
        result += '\n' + Node.title
        result += '\n' + self.iNode.__str__()
        result += '\n' + self.oNode.__str__()
       result += '\nQExtracted(kW): \t{:>.2f}'.format(self.QExtracted)    
        return result

