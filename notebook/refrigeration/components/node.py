import CoolProp.CoolProp as cp


class Node:

    title = ('{:^6} \t {:^30} \t {:<3}\t {:>10}\t {:>10}\t {:>10} \t {:>5}\t {:>15}'.format
             ("NodeID", "Name", "P(MPa)", "T(°C)", "H(kJ/kg)", "S(kJ/kg.K)",  "X", "MDOT(kg/s)"))

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
        self.stateok = False

        if self.t is not None and self.x is not None:
            self.tx()

    def tx(self):
        self.p = cp.PropsSI('P', 'T', 273.15+self.t,
                            'Q', self.x, 'R134a')/1.0e6
        self.h = cp.PropsSI('H', 'T', 273.15+self.t, 'Q', self.x, 'R134a')/1000
        self.s = cp.PropsSI('S', 'T', 273.15+self.t, 'Q', self.x, 'R134a')/1000
        self.stateok = True

    def ps(self):
        self.h = cp.PropsSI('H', 'P', self.p*1.0e6, 'S',
                            self.s*1000, 'R134a')/1000
        self.t = cp.PropsSI('T', 'P', self.p*1.0e6, 'S',
                            self.s*1000, 'R134a')-273.15
        self.stateok = True

    def setstate(self):
        if self.t is not None and self.x is not None:
            self.tx()
        if self.p is not None and self.s is not None:
            self.ps()

    def __str__(self):
        result = ('{:^6} \t {:<30}'.format(self.id, self.name))

        OutStrs = [{"fstr": '\t {:<6.3}', "sstr": '\t {:<6}', 'prop': self.p},
                   {"fstr": '\t {:>10.2f}', "sstr": '\t {:>10}', 'prop': self.t},
                   {"fstr": '\t {:>10.2f}', "sstr": '\t {:>10}', 'prop': self.h},
                   {"fstr": '\t {:>7.2f}', "sstr": '\t {:>7}', 'prop': self.s},
                   {"fstr": '\t {:>10.2f}', "sstr": '\t {:>10}', 'prop': self.x},
                   {"fstr": '\t {:>12.2f}', "sstr": '\t {:>12}', 'prop': self.mdot}
                   ]

        for item in OutStrs:
            try:
                result += item["fstr"].format(item["prop"])
            except:
                result += item["sstr"].format("")

        return result
