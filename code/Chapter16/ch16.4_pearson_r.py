import math

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_r(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)

x0=[10.0, 8.0,13.0, 9.0,11.0,
    14.0, 6.0, 4.0,12.0, 7.0,5.0]
y0=[8.04,6.95,7.58,8.81,8.33,
    9.96,7.24,4.26,10.84,4.82,5.68]
r=pearson_r(x0,y0)
print(r)

import numpy
numpy.corrcoef(x0,y0)[0, 1]
print(r)
