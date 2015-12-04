# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from seuif97 import *


def CylinderEff(cylinder):
    """simple function  for cylinde using 'dict' """

    cylinder['inlet']['h'] = pt2h(cylinder['inlet']['p'], cylinder['inlet']['t'])
    cylinder['inlet']['s'] = pt2s(cylinder['inlet']['p'], cylinder['inlet']['t'])

    cylinder['outlet']['h'] = pt2h(cylinder['outlet']['p'], cylinder['outlet']['t'])
    cylinder['outlet']['s'] = pt2s(cylinder['outlet']['p'], cylinder['outlet']['t'])

    # h2s is the specific enthalpy at state 2 for the isentropic turbine
    h2s = ps2h(cylinder['outlet']['p'], cylinder['inlet']['s'])
    
    cylinder['h2s'] = h2s
     
    hds = cylinder['inlet']['h'] - h2s  # isentropic specific enthalpy drop
    hd = cylinder['inlet']['h'] - cylinder['outlet']['h']  # specific enthalpy drop

    cylinder['ef'] = 100 * hd / hds

    return cylinder

def linepoint3(sstep,p,t,h,s,sis=None):
    if sis==None:
        s0 = s - sstep
    else:
        s0=sis-sstep  
    s2 = s + sstep
    point_h = np.zeros(shape=3)
    point_h[0] = ps2h(p, s0)
    point_h[1] = h
    point_h[2] = ps2h(p, s2)
    point_s = np.zeros(shape=3)
    point_s[0] = s0
    point_s[1] = s
    point_s[2] = s2
    return point_s,point_h


def linepoint2(h0,h1,s0,s1):
    point_h = np.zeros(shape=2)
    point_h[0] = h0
    point_h[1] = h1
    point_s = np.zeros(shape=2)
    point_s[0] = s0
    point_s[1] = s1
    return point_s,point_h

def CylinderPlot(cylinder):
    # 4条线：p1、p2 等压，等熵焓降线、膨胀线

    p1 = cylinder['inlet']['p']
    t1 = cylinder['inlet']['t']
    s1 = cylinder['inlet']['s']
    h1 = cylinder['inlet']['h']
    
    p2 = cylinder['outlet']['p']
    t2 = cylinder['outlet']['t']
    s2 = cylinder['outlet']['s']
    h2 = cylinder['outlet']['h']
    
    ef = cylinder['ef']
    
    hs = cylinder['h2s']
    
    point_p1_s,point_p1_h=linepoint3(0.01,p1,t1,h1,s1)
    point_p2_s,point_p2_h=linepoint3(0.01,p2,t2,h2,s2,s1)
    point_is_s,point_is_h=linepoint2(h1,hs,s1,s1)
    point_hp_s,point_hp_h=linepoint2(h1,h2,s1,s2)
    
    plt.plot(point_p1_s, point_p1_h, 'bs-')
    plt.plot(point_p2_s, point_p2_h, 'bs-')
    plt.plot(point_is_s, point_is_h, 'rs--')
    plt.plot(point_hp_s, point_hp_h, 'rs-', label='HP Expansion Line"')
    plt.minorticks_on()
    
    _title = 'The isentropic efficiency = ' + \
    r'$\frac{h1-h2}{h1-h2s}$' + '=' + '{:.2f}'.format(ef) + '%'
    plt.legend(loc="center left", bbox_to_anchor=[0.5, 0.5],
           ncol=2, shadow=True, title=_title)

    # annotate some interesting points using the annotate command
    plt.annotate('(P1,T1)',
             xy=(s1, h1), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plt.annotate('(P2,T2)',
             xy=(s2, h2), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plt.xlabel('s(kJ/(kg.K))')
    plt.ylabel('h(kJ/kg)')
    plt.show()


