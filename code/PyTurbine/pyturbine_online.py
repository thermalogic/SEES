# -*- coding: utf-8 -*-

from pyturbine import *
from pyredis import *

# 2.5.1 Set Tags
unittagdeflist=[]
unittagdeflist.append({'id':"CSDC.DCS2AI.2JZA2226",'desc':"二号机组高压缸入口压力"})
unittagdeflist.append({'id':"CSDC.DCS2AI.2JZA2408",'desc':"二号机组高压缸入口温度"})
unittagdeflist.append({'id':"CSDC.DCS2AI.2JZA2230",'desc':"二号机组高压缸出口压力"})
unittagdeflist.append({'id':"CSDC.DCS2AI.2JZA2459",'desc':"二号机组高压缸出口温度"})

TagDefToRedisHashKey(unittagdeflist)

unittagdeflist=[]
unittagdeflist.append({'id':"CSDC.DCS2AO.HP_EFF_IS",'desc':"二号机组高压缸等熵效率"})

TagDefToRedisHashKey(unittagdeflist)

# 2.5.2 Send run data to redis
    
unittagvaluelist=[]
unittagvaluelist.append({'id':"CSDC.DCS2AI.2JZA1030",'value':16.38525})
unittagvaluelist.append({'id':"CSDC.DCS2AI.2JZA2408",'value':538.37})
unittagvaluelist.append({'id':"CSDC.DCS2AI.2JZA2230",'value':3.035039})
unittagvaluelist.append({'id':"CSDC.DCS2AI.2JZA2459",'value':313.2931})
SendToRedisHash(unittagvaluelist)

# 3.1 get data form redis
unittaglist=[]
unittaglist.append({'id':"CSDC.DCS2AI.2JZA1030"})
unittaglist.append({'id':"CSDC.DCS2AI.2JZA2408"})
unittaglist.append({'id':"CSDC.DCS2AI.2JZA2230"})
unittaglist.append({'id':"CSDC.DCS2AI.2JZA2459"})
tagvalue_redis(unittaglist)

# 3.2 calc
hp = {'inlet':{}, 'outlet':{}, 'h2s':None, 'ef':None}
minlet = {'p':None, 't': None, 'h': None, 's':None}
moutlet = {'p': None, 't': None, 'h': None, 's': None}

minlet['p']=float(unittaglist[0]['value'])
minlet['t']=float(unittaglist[1]['value'])
moutlet['p']=float(unittaglist[2]['value'])
moutlet['t']=float(unittaglist[3]['value'])

hp['inlet'] = dict(minlet)
hp['outlet'] = dict(moutlet)
hp = CylinderEff(hp)
CylinderPlot(hp)

# 3.3 send result to redis
unittagvaluelist=[]
unittagvaluelist.append({'id':"CSDC.DCS2AO.HP_EFF_IS",'value':hp['ef']})
SendToRedisHash(unittagvaluelist)

# 2.5.4 get data form redis
unittaglist=[]
unittaglist.append({'id':"CSDC.DCS2AO.HP_EFF_IS"})
tagvalue_redis(unittaglist)

print(unittaglist[0]['value'])

