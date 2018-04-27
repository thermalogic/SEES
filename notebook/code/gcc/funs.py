
from ctypes import c_int,c_long,c_double,c_void_p,cdll
import numpy as np

_lib = cdll.LoadLibrary('./code/gcc/libfuns.dll')
#_lib = np.ctypeslib.load_library('libfuns', '.')

_lib.hello.argtypes = []
_lib.hello.restype  =  c_void_p

_lib.dprod.argtypes = [np.ctypeslib.ndpointer(dtype=np.float), c_int]
_lib.dprod.restype  = c_double

_lib.LinearFibonacci.argtypes = [c_int]
_lib.LinearFibonacci.restype= c_long


def hello():
    return _lib.hello()

def dprod(x):
    n = len(x)
    x = np.asarray(x, dtype=np.float)
    return _lib.dprod(x, int(n))

def LinearFibonacci(n):
    return _lib.LinearFibonacci(int(n))