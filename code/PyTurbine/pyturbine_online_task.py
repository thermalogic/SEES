# -*- coding: utf-8 -*-
from pyredis import *
from pyturbine import *
from datetime import datetime

class UnitHP:

    def __init__(self):
        self.ailist = []
        self.ailist.append({'id':"CSDC.DCS2AI.2JZA2226"})  # Pi
        self.ailist.append({'id':"CSDC.DCS2AI.2JZA2408"})  # Ti
        self.ailist.append({'id':"CSDC.DCS2AI.2JZA2230"})  # Po 
        self.ailist.append({'id':"CSDC.DCS2AI.2JZA2459"})  # To 
        self.ailist.append({'id':"CSDC.DCS2AI.2JZA2264"})  # Pamp
    
        self.aolist = []
        self.aolist.append({'id':"CSDC.DCS2AO.HP_EFF_IS", 'desc':"二号机组高压缸内效率", 'value':None, 'ts':None})
 
    def setouttag(self):
        TagDefToRedisHashKey(self.aolist)
 
    def Onlinecal(self):
   
        pam = float(self.ailist[4]['value']) / 1000
     
        hp = {'inlet':{}, 'outlet':{}, 'h2s':None, 'ef':None}
        minlet = {'p':None, 't': None, 'h': None, 's':None}
        moutlet = {'p': None, 't': None, 'h': None, 's': None}

        minlet['p'] = float(self.ailist[0]['value']) + pam
        minlet['t'] = float(self.ailist[1]['value'])
        moutlet['p'] = float(self.ailist[2]['value']) + pam
        moutlet['t'] = float(self.ailist[3]['value'])

        hp['inlet'] = dict(minlet)
        hp['outlet'] = dict(moutlet)
    
        hp = CylinderEff(hp)
    
        self.aolist[0]['value'] = hp['ef']
    
        return hp
    
    def run(self):
       
        tagvalue_redis(self.ailist)
        
        self.Onlinecal()
                
        curtime = datetime.now()
        for tag in self.aolist:
            tag['ts'] = curtime 

        SendToRedisHash(self.aolist)

        tagvalue_redis(self.aolist)
        
        for tag in self.aolist:
            print(tag['desc'], tag['value'])

