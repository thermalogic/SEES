#coding: utf-8 -*- 

#coding: utf-8 -*- 
# HP of 300MW Unit
#    LOAD 252.4395 MW
#    QMS 750.1908 t/h# HP of 300MW Unit

from seuif97 import *

pam=0.1005281

p10=16.17891+pam
t10=532.9128
p11=16.14941+pam
t11=535.2093

p2=3.845215+pam
t2=344.3879

h10=pt2h(p10,t10)
s10=pt2s(p10,t10)

h11=pt2h(p11,t11)
s11=pt2s(p11,t11)

h2=pt2h(p2,t2)
s2=pt2s(p2,t2)

h3=ps2h(p2,s11)
hdis13=h11-h3   # 等熵焓降
hd112=h11-h2     # 过程焓降

ieff=100*hd112/hdis13

h4=ps2h(p2,s10)
hdis14=h10-h4   # 等熵焓降
hd102=h10-h2     # 过程焓降

eeff=100*hd102/hdis14

print(h10,s10)
print(h11,s11)

print('internal efficiency: ',ieff)


import matplotlib.pyplot as plt
import numpy as np
import string


# p10等压，等熵降线、膨胀线
s_step=0.01

smp10=s10-s_step
hsmp10=ps2h(p10,smp10)
sap10=s10+s_step
hsap10=ps2h(p10,sap10)

point_p10_h=np.zeros(shape=3)
point_p10_h[0]=hsmp10
point_p10_h[1]=h10
point_p10_h[2]=hsap10
point_p10_s=np.zeros(shape=3)
point_p10_s[0]=smp10
point_p10_s[1]=s10
point_p10_s[2]=sap10

# p11等压

s_step=0.02

smp11=s11-s_step
hsmp11=ps2h(p11,smp11)
sap11=s11+s_step
hsap11=ps2h(p11,sap11)

point_p11_h=np.zeros(shape=3)
point_p11_h[0]=hsmp11
point_p11_h[1]=h11
point_p11_h[2]=hsap11
point_p11_s=np.zeros(shape=3)
point_p11_s[0]=smp11
point_p11_s[1]=s11
point_p11_s[2]=sap11

# p2等压线
s_step=0.01
smp2=s11-s_step 
hsmp2=ps2h(p2,smp2)
sap2=s2+s_step 
hsap2=ps2h(p2,sap2)

point_p2_h=np.zeros(shape=3)
point_p2_h[0]=hsmp2
point_p2_h[1]=h2
point_p2_h[2]=hsap2

point_p2_s=np.zeros(shape=3)
point_p2_s[0]=smp2
point_p2_s[1]=s2
point_p2_s[2]=sap2

# p11-p2等熵降线
point_is_h11_2=np.zeros(shape=2)
point_is_h11_2[0]=h11
point_is_h11_2[1]=h3
point_is_s11_2=np.zeros(shape=2)
point_is_s11_2[0]=s11
point_is_s11_2[1]=s11

# p11-p2 Expansion Line
point_hp_h11_2=np.zeros(shape=2)
point_hp_h11_2[0]=h11
point_hp_h11_2[1]=h2
point_hp_s11_2=np.zeros(shape=2)
point_hp_s11_2[0]=s11
point_hp_s11_2[1]=s2 

# p10-p2等熵降线
point_is_h10_2=np.zeros(shape=2)
point_is_h10_2[0]=h10
point_is_h10_2[1]=h4
point_is_s10_2=np.zeros(shape=2)
point_is_s10_2[0]=s10
point_is_s10_2[1]=s10

# p10-p2 Expansion Line
point_hp_h10_2=np.zeros(shape=2)
point_hp_h10_2[0]=h10
point_hp_h10_2[1]=h2
point_hp_s10_2=np.zeros(shape=2)
point_hp_s10_2[0]=s10
point_hp_s10_2[1]=s2 


plt.plot(point_p10_s,point_p10_h,'bs-',label="...")

plt.plot(point_p11_s,point_p11_h,'bs-')

plt.plot(point_p2_s,point_p2_h,'bs-')

plt.plot(point_is_s11_2,point_is_h11_2,'gs-')
plt.plot(point_hp_s11_2,point_hp_h11_2,'rs-')

plt.plot(point_is_s10_2,point_is_h10_2,'gs-')
plt.plot(point_hp_s10_2,point_hp_h10_2,'rs-')

plt.minorticks_on()
plt.legend(loc="center left", bbox_to_anchor=[0.5, 0.5],
        ncol=2, shadow=True, title='HP Expansion Line')
#annotate some interesting points using the annotate command
plt.annotate('(P0)',
         xy=(s10, h10), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=12,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.annotate('(P1)',
         xy=(s11, h11), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=12,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.annotate('(P2)',
         xy=(s2, h2), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=12,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.xlabel('s')
plt.ylabel('h')
plt.show()

print('external efficiency: ',eeff)
