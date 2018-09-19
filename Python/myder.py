# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:50:22 2018

@author: Tom K
"""
import numpy as np
from numpy import array

def simpleder(a):
   # da = np.diff(a)
    #db = np.diff(a)/np.diff(b) 
    da = np.gradient(a)
   # return array(da), array(db)
    return array(da)

def forwardiff(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(1,N):
        slop = (f(a+k*h)-f(a+(k-1)*h))/h
        g.append(slop)
    return array(g)

def backwardiff(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(0,N-1):
        slop = (f(a+(k+1)*h)-f(a+k*h))/h
        g.append(slop)
    return array(g)

def centraldiff(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(0,N):
        slop = (f(a+(k+1/2)*h)-f(a+(k-1/2)*h))/h
        g.append(slop)
    return array(g)

def centraldiffcubic(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(0,N):
        slop = ((1/24)*f(a+(k-3/2)*h)-(27/24)*f(a+(k-1/2)*h)+(27/24)*f(a+(k+1/2)*h)-(1/24)*f(a+(k+3/2)*h))/h
        g.append(slop)
    return array(g)

