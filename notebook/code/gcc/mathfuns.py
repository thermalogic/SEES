
from ctypes import windll,c_double

flib = windll.LoadLibrary('./code/gcc/libmathfuns.dll')


def fadd(a,b):
    flib.fadd.argtypes = [c_double,c_double]
    flib.fadd.restype  = c_double
    return flib.fadd(a,b)

def fmul(a,b):
    flib.fmul.argtypes = [c_double,c_double]
    flib.fmul.restype  = c_double
    return flib.fmul(a,b)