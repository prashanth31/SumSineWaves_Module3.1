"""
Prashanth Khambhammettu (prashanth31@gmail.com)
2013/02/20 : Summation of Sine Waves
"""

import matplotlib.pyplot as plt
import numpy as np
import math as math 
import sys

"""
Sine function
Returns an array of times and values of sin(pi*n*t) /n 
where t belongs to [-1,1]

n is the input parameter
"""
def xn(n):
    if(n==0):
        sys.exit('Cannot divide by zero')
        
    pi=math.pi
    delta=1e-04
    t= np.arange(-1,1+delta,delta)
    #print t.shape
    y=np.empty(t.shape, dtype=float)
    #print y.shape
    y=np.sin(pi*n*t)
    return t,y/n
    

"""
Summation function
Sums several xn functions
Calculates sigma(xn(2K+1)) for k=0 to N
returns an array of times and summation values
"""
def summation(N):
    if(N<0):
        sys.exit('Cannot Compute when N is less than 0')
    #Compute the first wave
    t,y = xn(2*0+1)
    #Add the remaining waves when we have more than one
    if(N>0):
        for k in range(1,N+1):
            t,ynew=xn(2*k+1)
            y=y+ynew
    return t,y
            


""" Main part of the program """
ax1 =plt.subplot(2,2,1)
t1,y1 =summation(0)
ax1.plot(t1,y1,'r-')
ax1.grid(which='both')
plt.title ('N=0')


ax2 =plt.subplot(2,2,2)
t2,y2 =summation(2)
ax2.plot(t2,y2,'r-')
ax2.grid(which='both')
plt.title ('N=2')


ax3 =plt.subplot(2,2,3)
t3,y3 =summation(20)
ax3.plot(t3,y3,'r-')
ax3.grid(which='both')
plt.title ('N=20')

ax4 =plt.subplot(2,2,4)
t4,y4 =summation(150)
ax4.plot(t4,y4,'r-')
ax4.grid(which='both')
plt.title ('N=150')

plt.xlim(-1,1)
plt.ylim(-1,1)

plt.show()