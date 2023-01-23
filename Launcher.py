import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
from sympy import symbols, Eq, solve , exp , sin , cos
from scipy.optimize import fsolve


#####DATA######
#math constants 
pi = 3.14159265359 
g = 9.81

#wheel velocity 

rpm = 3400
W = (rpm/60) * 2 * pi
r = 0.09

#tennisbal constants

k = 1.5

C = 0.5
rho = 1.292
A = 0.003316625

cor = 0.66666
cof = 0.72

#launcher constants

s0 = 1

#########################

global distance 





def first_bounce(x):

    y = 0
    def equations(vars):
        v0, t = vars
        eq1 = (((x)*k) / (-exp(-k*t)+1))/cos(theta)-v0
        eq2 = ((k*(y+1)-g/k+g*t-((g/k)*exp(-k*t)))/(exp(-k*t)+1))/sin(theta)-v0
        return [eq1, eq2 ] 
    v0 , t = fsolve(equations, (1,1))
    print(v0)
    return(v0)





def projecting(v0 , theta):
    v0x = v0 * cos(theta)
    v0y = v0 * sin(theta)
    A = g/k
    B = v0y + A
    cx = -v0x/-k * exp(0*-k)
    cy = B/-k * exp(0*-k)-A*0
    i = 0 
    x1 = []
    y1 = []
    t = 0
    tf = 3.0*v0y/g
    dt = tf/2000
    while B/-k * exp(t*-k)-A*t-(cy-1) >= 0: 
        t = t + dt
        x1.append(v0x/-k * exp(t*-k)+cx)
        y1.append(B/-k * exp(t*-k)-A*t-(cy-1)) 
        #print(x[i],y[i])
        i = i + 1
    v0x2 = v0x * cof
    v0y2 = -(v0y-g*t) * cor
    xref = x1[i-1]
    t = 0 
    tf = 2.0*v0/g
    dt = tf/2000
    A = g/k
    B = v0y2 + A
    cx = -v0x2/-k * exp(0*-k)
    cy = B/-k * exp(0*-k)-A*0
    while B/-k * exp(t*-k)-A*t-(cy) >= 0:
        t = t + dt 
        x1.append(v0x2 /-k * exp(t*-k)+cx + xref)
        y1.append(B/-k * exp(t*-k)-A*t-cy) 
        #print(x[i],y[i])
        i = i + 1 
    return[x1 , y1, i]


def calculating(theta, v0):
    variables = projecting(v0 , theta)
    x = variables[0]
    y = variables[1]
    i = variables[2]
 
    while (xend - x[i-1] > 0):
        if xend - x[i-1] > 0.1:
            v0 = v0 + 0.1
            projecting(v0 , theta)
            variables = projecting(v0 , theta)
            x = variables[0]
            y = variables[1]
            i = variables[2]
            print(x[i-1], v0 , theta/(pi/180))
    while (xend - x[i-1] < 0):
        if xend - x[i-1] < 0.1:
            v0 = v0 - 0.1
            projecting(v0 , theta)
            variables = projecting(v0 , theta)
            x = variables[0]
            y = variables[1]
            i = variables[2]
            print(x[i-1], v0 , theta/(pi/180))        
        
    return(x, y, theta, i , v0)

def start_program(distance,angle):
    global xend
    global xbounce
    global theta
    xend = int(distance)
    xbounce = cor * xend
    theta = int(angle)*(pi/180)
    v0 = first_bounce(xbounce)
    data_after_calc = calculating(theta, v0)
    v0 = data_after_calc[4]
    i = data_after_calc[3]
    angle = data_after_calc[2]
    yimpact = data_after_calc[1]
    ximpact = data_after_calc[0]

    print(ximpact[i-1],v0 , angle /(pi/180))
    rpm = ((v0 /(r*0.5))/(2*pi))*60
    df = pd.DataFrame(list(zip(ximpact,yimpact)),
            columns = ['xdata','ydata'])
    return(rpm)

