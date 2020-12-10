import CoolProp.CoolProp as cp


class Node:

    title = ('{:^6} \t {:^30} \t {:<3}\t {:>10}\t {:>10}\t {:>10} \t {:>10}\t {:>5}\t {:>15}'.format
             ("NodeID", "Name", "P(MPa)", "T(°C)", "H(kJ/kg)", "S(kJ/kg.K)", "V(m^3/kg)", "X", "MDOT(kg/s)"))

    def __init__(self, dictnode):
        """ create the node object"""

        self.name = dictnode['name']
        self.id = dictnode['id']

        try:
            self.t = float(dictnode['t'])
        except:
            self.t = None
        try:
            self.x = float(dictnode['x'])
        except:
            self.x = None

        try:
            self.mdot = float(dictnode['mdot'])
        except:
            self.mdot = None

        self.p = None
        self.h = None
        self.s = None
        self.v = None
        self.stateok = False

        if self.t is not None and self.x is not None:
            self.tx()

    def tx(self):
        self.p = cp.PropsSI('P', 'T', 273.15+self.t,
                            'Q', self.x, 'R134a')/1.0e6
        self.h = cp.PropsSI('H', 'T', 273.15+self.t, 'Q', self.x, 'R134a')/1000
        self.s = cp.PropsSI('S', 'T', 273.15+self.t, 'Q', self.x, 'R134a')/1000
        self.v = cp.PropsSI('V', 'T', 273.15+self.t, 'Q', self.x, 'R134a')/1000
        self.stateok = True

    def ps(self):
        self.h = cp.PropsSI('H', 'P', self.p*1.0e6, 'S',self.s*1000, 'R134a')/1000
        self.t = cp.PropsSI('T', 'P', self.p*1.0e6, 'S',self.s*1000, 'R134a')-273.15
        self.x = cp.PropsSI('Q', 'P', self.p*1.0e6, 'S',self.s*1000, 'R134a')/1000
        self.v = cp.PropsSI('V', 'P', self.p*1.0e6, 'S', self.s*1000, 'R134a')/1000
        self.stateok = True


    def setstate(self):
        if self.t is not None and self.x is not None:
            self.tx()
        if self.p is not None and self.s is not None:
            self.ps()

    def __str__(self):
        try:
            result = ('{:^6} \t {:<30} \t {:>6.3}\t {:>10.2f}\t {:>10.2f}\t {:>5.2f} \t {:>15.3f}\t {:>5.3}\t {:>12.2f}'.format
                      (self.id, self.name, self.p, self.t, self.h, self.s, self.v, self.x, self.mdot))
        except:
            result = ('{:^6} \t {:<30}'.format(self.id, self.name))
            
            if self.p is not None:
                result +=('\t {:<6.3}'.format(self.p))
            else:
                result += ('\t {:<6}'.format(""))
            
            if self.t is not None:
                result +=('\t {:>10.2f}'.format(self.t))
            else:
                result += ('\t {:>10}'.format(""))

            if self.h is not None:
                result +=('\t {:>10.2f}'.format(self.h))
            else:
                result += ('\t {:>10}'.format(""))

            if self.s is not None:
                result +=('\t {:>5.2f}'.format(self.s))
            else:
                result += ('\t {:>5}'.format(""))
                
            if self.v is not None:
                result +=('\t {:>15.3f}'.format(self.v))
            else:
                result += ('\t {:>15}'.format(""))
            
            if self.x is not None:
                result +=('\t {:>5.3f}'.format(self.x))
            else:
                result += ('\t {:>5}'.format(""))
            
            if self.mdot is not None:
                result +=('\t {:>12.2f}'.format(self.mdot))
            else:
                result += ('\t {:>12}'.format(""))
        # string   
        return result
