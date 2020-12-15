
from ctypes import windll,c_double,WINFUNCTYPE

flib = windll.LoadLibrary('./bin/libR134aSat.dll')
prototype = WINFUNCTYPE(c_double,c_double)

def pSat(t):
    f = prototype(("pSat", flib),)
    return f(t)
