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
    
    samp = 0.01
     
    smp1 = s1 - samp
    hsmp1 = ps2h(p1, smp1)
    sap1 = s1 + samp
    hsap1 = ps2h(p1, sap1)

    smt1 = s1 - samp
    hsmt1 = ps2h(p1, smp1)
    sat1 = s1 + samp
    hsat1 = ts2h(t1, sap1)
    
    # 1 p1等压
    point_p1_h = np.zeros(shape=3)
    point_p1_h[0] = hsmp1
    point_p1_h[1] = h1
    point_p1_h[2] = hsap1
    point_p1_s = np.zeros(shape=3)
    point_p1_s[0] = smp1
    point_p1_s[1] = s1
    point_p1_s[2] = sap1

    # 2 p2 等压
    smp2 = s1 - samp  # 等熵焓降点延伸
    hsmp2 = ps2h(p2, smp2)
    sap2 = s2 + samp
    hsap2 = ps2h(p2, sap2)

    smt2 = s2 - samp
    hsmt2 = ps2h(p1, smp1)
    sat2 = s2 + samp
    hsat2 = ts2h(t2, sap1)

    point_p2_h = np.zeros(shape=3)
    point_p2_h[0] = hsmp2
    point_p2_h[1] = h2
    point_p2_h[2] = hsap2

    point_p2_s = np.zeros(shape=3)
    point_p2_s[0] = smp2
    point_p2_s[1] = s2
    point_p2_s[2] = sap2

    # 3 等熵焓降
    point_is_h = np.zeros(shape=2)
    point_is_h[0] = h1
    point_is_h[1] = hs
    point_is_s = np.zeros(shape=2)
    point_is_s[0] = s1
    point_is_s[1] = s1

    # 4 HP Expansion Line
    point_hp_h = np.zeros(shape=2)
    point_hp_h[0] = h1
    point_hp_h[1] = h2
    point_hp_s = np.zeros(shape=2)
    point_hp_s[0] = s1
    point_hp_s[1] = s2

    plt.plot(point_p1_s, point_p1_h, 'bs-', label='iP')

    plt.plot(point_p2_s, point_p2_h, 'bs-', label=r'$\frac{1}{2}\pi$')
    plt.plot(point_is_s, point_is_h, 'rs-', label='is')
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


