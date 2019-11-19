from ctypes import windll,c_double,WINFUNCTYPE

flib = windll.LoadLibrary('./demo/bin/libregion4.dll')

def pSat(T):
    dT=c_double(T)
    f =flib.pSat
    return f(dT)

def TSat(p):
    dp=c_double(p)
    f =flib.TSat
    return f(dp)
