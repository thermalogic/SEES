# -*- coding: utf-8 -*-

from pyturbine import *
from pyredisserver import *

hp = {'inlet':{}, 'outlet':{}, 'h2s':None, 'ef':None}
minlet = {'p':None, 't': None, 'h': None, 's':None}
moutlet = {'p': None, 't': None, 'h': None, 's': None}

minlet['p']=16.38525
minlet['t']=538.37
moutlet['p']=3.035039
moutlet['t']=313.2931

hp['inlet'] = dict(minlet)
hp['outlet'] = dict(moutlet)
hp = CylinderEff(hp)
CylinderPlot(hp)


