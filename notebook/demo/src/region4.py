
from ctypes import windll,c_double

flib = windll.LoadLibrary('./demo/bin/libregion4.dll')

def pSat(T):
    flib.pSat.argtypes = [c_double]
    flib.pSat.restype  = c_double
    return flib.pSat(T)

def TSat(p):
    flib.TSat.argtypes = [c_double]
    flib.TSat.restype  = c_double
    return flib.TSat(p)
