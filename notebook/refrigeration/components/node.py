
"""
The Object-oriented Programming Demo of  VCR Cycle
    Node
"""
import CoolProp.CoolProp as cp

class Node:

    title = ('{:^6} \t{:^32} \t{:<8} \t{:>8} \t{:>10} \t{:>10} \t{:^10} \t{:>10}'.format
             ("NodeID", "Name", "P(MPa)", "T(°C)", "H(kJ/kg)", "S(kJ/kg.K)",  "Quality", "MDOT(kg/s)"))

    def __init__(self, dictnode):
        """ create the node object"""

        self.name = dictnode['name']
        self.id = dictnode['id']

        try:
            self.p = float(dictnode['p'])
        except:
            self.p = None
        
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

        self.h = None
        self.s = None
        self.stateok = False

        if self.t is not None and self.x is not None:
            self.tx()
        elif self.p is not None and self.x is not None:
            self.px()
        elif self.p is not None and self.t is not None:
            self.pt()

    def tx(self):
        try:
           self.p = cp.PropsSI('P', 'T', 273.15+self.t,
                            'Q', self.x, 'R134a')/1.0e6
           self.h = cp.PropsSI('H', 'T', 273.15+self.t, 'Q', self.x, 'R134a')/1000
           self.s = cp.PropsSI('S', 'T', 273.15+self.t, 'Q', self.x, 'R134a')/1000
           self.stateok = True
        except:
            self.stateok = False
        
    def px(self):
        try:
           self.t = cp.PropsSI('T', 'P', self.p*1.0e6,'Q', self.x, 'R134a')-273.15
           self.h = cp.PropsSI('H', 'P', self.p*1.0e6, 'Q', self.x, 'R134a')/1000
           self.s = cp.PropsSI('S', 'P', self.p*1.0e6, 'Q', self.x, 'R134a')/1000
           self.stateok = True
        except:
            self.stateok = False
      
    def pt(self):
        try:
            self.h = cp.PropsSI('H', 'P', self.p*1.0e6,'T', self.t+273.15, 'R134a')/1000
            self.s = cp.PropsSI('S', 'P', self.p*1.0e6, 'T', self.t+273.15, 'R134a')/1000
            self.x = cp.PropsSI('Q', 'P', self.p*1.0e6, 'H', self.h*1000, 'R134a')
            if self.x == -1:
                self.x = None
            self.stateok = True
        except:
            self.stateok = False
      
    def ps(self):
        try:
            if self.h is None:
                self.h = cp.PropsSI('H', 'P', self.p*1.0e6, 'S',
                            self.s*1000, 'R134a')/1000
            if self.t is None:
               self.t = cp.PropsSI('T', 'P', self.p*1.0e6, 'S',
                            self.s*1000, 'R134a')-273.15
            if self.x is None:
                self.x = cp.PropsSI('Q', 'P', self.p*1.0e6, 'S',
                            self.s*1000, 'R134a')
                if self.x == -1:
                    self.x = None
            self.stateok = True
        except:
            self.stateok = False
        

    def ph(self):
        try:
            if self.s is None:
                self.s = cp.PropsSI('S', 'P', self.p*1.0e6, 'H',
                                self.h*1000, 'R134a')/1000
            if self.t is None:
                self.t = cp.PropsSI('T', 'P', self.p*1.0e6, 'H',
                                self.h*1000, 'R134a')-273.15
            if self.x is None:
                self.x = cp.PropsSI('Q', 'P', self.p*1.0e6, 'H',
                                self.h*1000, 'R134a')
                if self.x == -1:
                    self.x = None
            self.stateok = True
        except:
            self.stateok = False
           

    def setstate(self):
        if self.stateok == False:
            if self.p is not None and self.s is not None:
               self.ps()
            elif self.p is not None and self.h is not None:
               self.ph()
       
    def __str__(self):
        result = ('{:^6} \t{:<32}'.format(self.id, self.name))

        OutStrs = [{"fstr": '\t{:>7.4}', "sstr": '\t{:>7}', 'prop': self.p},
                   {"fstr": '\t{:>8.2f}', "sstr": '\t{:>8}', 'prop': self.t},
                   {"fstr": '\t{:>10.2f}', "sstr": '\t{:>10}', 'prop': self.h},
                   {"fstr": '\t{:>8.3f}', "sstr": '\t{:>8}', 'prop': self.s},
                   {"fstr": '\t{:>10.4f}', "sstr": '\t{:>10}', 'prop': self.x},
                   {"fstr": '\t{:>8.2f}', "sstr": '\t{:>8}', 'prop': self.mdot}
                   ]

        for item in OutStrs:
            try:
                result += item["fstr"].format(item["prop"])
            except:
                result += item["sstr"].format("")

        return result
