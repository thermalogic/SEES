
from ctypes import windll,c_double,WINFUNCTYPE

flib = windll.LoadLibrary('./bin/libregion4.dll')
prototype = WINFUNCTYPE(c_double,c_double)

def pSat(T):
    f = prototype(("pSat", flib),)
    return f(T)

def TSat(p):
    f = prototype(("TSat", flib),)
    return f(p)
