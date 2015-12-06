# -*- coding: utf-8 -*-
import threading
from pyredis import *
from datetime import datetime
import time
import random

class UnitHPSimulation:

    def __init__(self, delay,):
        self.delay = delay
        self.next_call = time.time()
        
        self.ailist = []
        self.ailist.append({'id':"CSDC.DCS2AI.2JZA2226", 'desc':"二号机组高压缸入口压力", 'value':16.38525})  # Pi
        self.ailist.append({'id':"CSDC.DCS2AI.2JZA2408", 'desc':"二号机组高压缸入口温度", 'value':538.37})  # Ti
        self.ailist.append({'id':"CSDC.DCS2AI.2JZA2230", 'desc':"二号机组高压缸出口压力", 'value':3.035039})  # Po 
        self.ailist.append({'id':"CSDC.DCS2AI.2JZA2459", 'desc':"二号机组高压缸出口温度", 'value':313.2931})  # To 
        self.ailist.append({'id':"CSDC.DCS2AI.2JZA2264", 'desc':"大气压力", 'value':100.5281})  # Pamp
        
        self.pibase = self.ailist[0]['value'] 
  
    def settag(self):
        TagDefToRedisHashKey(self.ailist)
 
    def run(self):
        self.ailist[0]['value'] = self.pibase * (1 + random.random() * 0.01)
        
        curtime = datetime.now()
        for tag in self.ailist:
            tag['ts'] = curtime 
        SendToRedisHash(self.ailist)

        print(self.ailist[0]['value'])

    def worker(self):
        self.run()
        self.next_call = self.next_call + self.delay
        threading.Timer(self.next_call - time.time(), self.worker).start()
        
if __name__ == "__main__":
    
    UnitHPSimu = UnitHPSimulation(5)
    UnitHPSimu.settag()
    UnitHPSimu.worker()
 
   
