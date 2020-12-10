import CoolProp.CoolProp as cp


class Node:

    title = ('{:^6} \t {:^20} \t {:^5}\t {:^7}\t {:^7}\t {:^5} \t {:^7} \t{:^7}'.format
             ("NodeID", "Name", "P", "T", "H", "S", "X","MDOT"))

    def __init__(self, name, nid):
        self.name = name
        self.nid = nid
        self.p = None
        self.t = None
        self.h = None
        self.s = None
        self.mdot = None
    
    def tx(self):
        self.p=cp.PropsSI('P', 'T', 273.15+self.t, 'Q',x, 'R134a')/1.0e6
        self.h=cp.PropsSI('H', 'T', 273.15+self.t, 'Q',x, 'R134a')/1000
        self.s=cp.PropsSI('S', 'T', 273.15+self.t, 'Q',x, 'R134a')/1000
 
    def ps(self):
        self.h=cp.PropsSI('H', 'P',self.p*1.0e6, 'S',self.s*1000, 'R134a')/1000
        self.t=cp.PropsSI('T', 'P',self.p*1.0e6, 'S',self.s*1000, 'R134a')-273.15
        self.x=cp.PropsSI('Q', 'P',self.p*1.0e6, 'S',self.s*1000, 'R134a')/1000;
            
    
    def __str__(self):
        result = ('{:^6d} \t {:^20} \t {:>5.2f}\t {:>7.3f}\t {:>7.2f}\t {:>5.2f}t {:>5.2f} {:>5.3}'.format
                  (self.nid, self.name, self.p, self.t, self.h, self.s, self.x,self.mdot))
        return result
