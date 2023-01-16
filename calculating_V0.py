import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
from sympy import symbols, Eq, solve
from sympy import exp 
from sympy import sin 
from sympy import cos 
from scipy.optimize import fsolve , root


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





y = 0 
x = 12

""""
def equations(vars):
    v0, t = vars
    eq1 = (((x)*k) / (-exp(-k*t)+1))/cos(theta)-v0
    eq2 = ((k*(y+1)-g/k+g*t-((g/k)*exp(-k*t)))/(exp(-k*t)+1))/sin(theta)-v0
    return [eq1, eq2 ]

v0 , t = fsolve(equations, (1,1))
print(v0,t)
"""

def equations(vars):
    v0, t ,x1 ,x2 = vars
    eq1 = (((12-x2)*k) / (-exp(-k*t)+1))/cos(theta)-v0
    eq2 = ((k*(y+1)-g/k+g*t-((g/k)*exp(-k*t)))/(exp(-k*t)+1))/sin(theta)-v0
    eq3 = (((12-x1)*k) / (-exp(-k*t)+1))/(cos(theta)*cof)-v0
    eq4 = (((k*y)-(g/k)+(g*t)-(g/k * exp(-k*t)))/((exp(-k*t))*cor)+g*t)+v0
   
    return [eq1, eq2, eq3, eq4]


initialGuess = [1,1,1,1]
v0 , t, x1, x2 = fsolve(equations, initialGuess)

result = root(equations, initialGuess, method='lm')
print(result.x)