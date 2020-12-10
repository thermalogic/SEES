
"""
General Object-oriented Abstraction  of VPR Cycle 

The Simulator of vpr Cycle 

  * Input :vpr cycle dict model

  * output: text file

 
Run: 

python refrigerationapp.py
  

"""
from vprcycle.cycleobj import RefrigerationCycle
from vprcycle.cyclehelper import OutFiles
from cyclemodel import *
from platform import *

if __name__ == "__main__":
       
    curpath = os.path.abspath(os.path.dirname(__file__))
    ResultFilePath =curpath+'\\'+'./result/'
      
    for curcycle in cycles:
        ResultFileName=ResultFilePath+curcycle.cycle['name']

        cycle = RankineCycle(curcycle.cycle)
        cycle.simulator()
        # output to text
        OutFiles(cycle)
        OutFiles(cycle, ResultFileName + '.txt')

