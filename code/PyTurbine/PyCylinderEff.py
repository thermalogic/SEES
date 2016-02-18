#coding: utf-8 -*- 

# HP of 300MW Unit
#    LOAD 252.44 MW
#    QMS 750.19 t/h

from seuif97 import *

pam=0.10
p10=16.18+pam
t10=532.91
p11=16.15+pam
t11=535.21

p2=3.85+pam
t2=344.39

h10=pt2h(p10,t10)
s10=pt2s(p10,t10)

h11=pt2h(p11,t11)
s11=pt2s(p11,t11)

h2=pt2h(p2,t2)
s2=pt2s(p2,t2)

h3=ps2h(p2,s11)
hdis13=h11-h3   # 绛夌喌鐒撻檷
hd112=h11-h2     # 杩囩▼鐒撻檷

ieff=100*hd112/hdis13

h4=ps2h(p2,s10)
hdis14=h10-h4   # 绛夌喌鐒撻檷
hd102=h10-h2     # 杩囩▼鐒撻檷

eeff=100*hd102/hdis14

print(h10,s10)
print(h11,s11)

print('internal efficiency: ',ieff)
print('external efficiency: ',eeff)

import matplotlib.pyplot as plt
import numpy as np
import string

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

# p10绛夊帇
point_p10_s,point_p10_h=linepoint3(0.02,p10,t10,h10,s10)
# p11绛夊帇
point_p11_s,point_p11_h=linepoint3(0.02,p11,t11,h11,s11)

# p2绛夊帇绾�
point_p2_s,point_p2_h=linepoint3(0.02,p2,t2,h2,s2,s11)

# p11-p2绛夌喌闄嶇嚎
point_is_s11_2,point_is_h11_2=linepoint2(h11,h3,s11,s11)
# p11-p2 Expansion Line
point_hp_s11_2,point_hp_h11_2=linepoint2(h11,h2,s11,s2)
# p10-p2绛夌喌闄嶇嚎
point_is_s10_2,point_is_h10_2=linepoint2(h10,h4,s10,s10)
# p10-p2 Expansion Line
point_hp_s10_2,point_hp_h10_2=linepoint2(h10,h2,s10,s2)

plt.plot(point_p10_s,point_p10_h,'bs-')
plt.plot(point_p11_s,point_p11_h,'ys-')
plt.plot(point_p2_s,point_p2_h,'bs-')

plt.plot(point_is_s11_2,point_is_h11_2,'gs--')
plt.plot(point_hp_s11_2,point_hp_h11_2,'rs-',label=" ")

plt.plot(point_is_s10_2,point_is_h10_2,'gs--')
plt.plot(point_hp_s10_2,point_hp_h10_2,'rs-')

plt.minorticks_on()

_title =( 'The internal efficiency = ' +
    r'$\frac{h11-h2}{h11-h3}$' + '=' + '{:.2f}'.format(ieff) + '%'
          +'\n'+
          'The external efficiency = ' +
    r'$\frac{h10-h2}{h10-h4}$' + '=' + '{:.2f}'.format(eeff) + '%')
plt.legend(loc="center left", bbox_to_anchor=[0.5, 0.5],
        ncol=2, shadow=True, title= _title)
#annotate some interesting points using the annotate command
plt.annotate('H10',
         xy=(s10, h10), xycoords='data',
         xytext=(+5, +20), textcoords='offset points', fontsize=12,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.annotate('H11',
         xy=(s11, h11), xycoords='data',
         xytext=(+10, +20), textcoords='offset points', fontsize=12,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.annotate('H2',
         xy=(s2, h2), xycoords='data',
         xytext=(+5, +20), textcoords='offset points', fontsize=12,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.annotate('H3',
         xy=(s11, h3), xycoords='data',
         xytext=(+5, +20), textcoords='offset points', fontsize=12,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.annotate('H4',
         xy=(s10, h4), xycoords='data',
         xytext=(-15, +20), textcoords='offset points', fontsize=12,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.xlabel('s')
plt.ylabel('h')
plt.show()
