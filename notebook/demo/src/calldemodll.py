
from ctypes import *

flib = windll.LoadLibrary("dllTest")
f=flib.GetNumber
v=c_int(10)
print(f(byref(v)))
pi = pointer(v)
print(f(pi))

f.restype=c_int
f.restype.argtypes= [POINTER(c_int)]
print(f(pi))

prototype = WINFUNCTYPE(c_int,POINTER(c_int))
f = prototype(("GetNumber", flib),)
print(f(pi))
