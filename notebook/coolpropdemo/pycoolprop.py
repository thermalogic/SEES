from ctypes import *
lib = cdll.LoadLibrary("./coolpropdemo/bin/CoolProp_x64.dll")

def pt2h(p,t):
    PropsSI = lib.PropsSI
    PropsSI.argtypes = (c_char_p, c_char_p,c_double,c_char_p, c_double, c_char_p)
    PropsSI.restype = c_double
    result = PropsSI(b"H", b"T",t+273.15, b"P",p*1.0e6, create_string_buffer(b"Water"))/1000
    return  result 
