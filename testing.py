import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
from sympy import symbols, Eq, solve
from sympy import exp 
from sympy import sin 
from sympy import cos 
from scipy.optimize import fsolve


#math constants 
pi = 3.14159265359 
g = 9.81

#wheel velocity 

rpm = 3400
W = (rpm/60) * 2 * pi
r = 0.09
velocity = W * r * 0.5 


#tennisbal constants

k = 1.5

C = 0.5
rho = 1.292
A = 0.003316625

cor = 0.66666
cof = 0.72

#launcher constants

theta = 10*pi/180
s0 = 1



#### vergelijkingen





#xequation1 = (((x)*k) / (-exp(-k*t)+1))/cos(theta)-v0
#v0x_equation2 = ((x*k)/(-cof*exp(-k*t)+cof-exp(-k*t)+1))/cos(theta)-v0

"""
def equations(vars):
    v0, t = vars
    eq1 = ((x*k) / (-exp(-k*t)+1))/cos(theta)-v0
    eq2 = ((k*(y+1)-g/k+g*t-((g/k)*exp(-k*t)))/(exp(-k*t)+1))/sin(theta)-v0
    return [eq1, eq2]

v0 , t = fsolve(equations, (1,1))
print(v0,t)
"""
y = 0 
x = 8
def equations(vars):
    v0, t = vars
    eq1 = (((x)*k) / (-exp(-k*t)+1))/cos(theta)-v0
    eq2 = ((k*(y+1)-g/k+g*t-((g/k)*exp(-k*t)))/(exp(-k*t)+1))/sin(theta)-v0
    return [eq1, eq2 ]

v0 , t = fsolve(equations, (1,1))
print(v0,t)
