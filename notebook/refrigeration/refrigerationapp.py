
"""

The Object-oriented Programming Demo of VPR Cycle 

 * Input :vpr cycle dict model

 * Output: text file
 
Run: 

python refrigerationapp.py
  

"""
from vprcycle.cycleobj import RefrigerationCycle
from vprcycle.cyclehelper import OutFiles
from cyclemodel import cycles
from platform import os

if __name__ == "__main__":
       
    curpath = os.path.abspath(os.path.dirname(__file__))
    ResultFilePath =curpath+'\\'+'./result/'
      
    for curcycle in cycles:
        ResultFileName=ResultFilePath+curcycle.cycle['name']

        cycle = RefrigerationCycle(curcycle.cycle)
        cycle.simulator()
        # output to text
        OutFiles(cycle)
        OutFiles(cycle, ResultFileName + '.txt')

