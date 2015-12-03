# -*- coding: utf-8 -*-

import threading
from datetime import *
import time
from pyturbine_online_task import *
from pyredis import *

class PeriodTasks ():

    def __init__(self, delay, tasks):
        self.tasks = tasks
        self.delay = delay
        self.next_call = time.time()
  
    def setoutag(self):
        for task in self.tasks:
           task.setouttag()
    
    def worker(self):
        for task in self.tasks:
            task.run()
       
        self.next_call = self.next_call + self.delay
        threading.Timer(self.next_call - time.time(), self.worker).start()

if __name__ == "__main__":
    TaskList = []
    CurUnitHP = UnitHP()
    TaskList.append(CurUnitHP)
    
    OnlineTasks = PeriodTasks(2, TaskList)
    OnlineTasks.setoutag()
    OnlineTasks.worker()
 
   
