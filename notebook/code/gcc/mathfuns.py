
from ctypes import windll,c_int

flib = windll.LoadLibrary('libmathfuns.dll')


def add2(num):
    flib.add2.argtypes = [c_int]
    flib.add2.restype  = c_int
    return flib.add2(num)

def mult(num1,num2):
    flib.add2.argtypes = [c_int,c_int]
    flib.add2.restype  = c_int
    return flib.mult(num1,num2)
   