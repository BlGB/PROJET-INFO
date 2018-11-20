### TIPE : Résolution des équations différentielles pour un tir avec effet Magnus ###

# Voici les courbes de modélisation d'un tir soumis à l'effet magnus, avec plusieurs vitesses angulaires supposées constantes

## Définition des constantes ##

import math as mp
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

Cs=0.5
rho=1.23
m=0.0027
A=0.005
omega=5
r=0.04

C=0.5*(Cs*rho*A*omega*r)/m
g=9.8

## Définition de la fonction traduisant l'équation différentielle ##
def effet(w,t):
    x1,y1,x2,y2=w
    # On crée f=(x1',y1',x2',y2')
    f=[y1,
    -C*mp.sqrt((x1**2)+(x2**2)),
    y2,
    0]
    return f

## Conditions initiales et paramètres ##
# x1 et x2 sont les positions initiales, y1 et y2 les vitesses initiales
x1=0
x2=0
y1=0
y2=10

# Paramètres de résolution pour ODE
xlim=1.0e-8
ylim=1.0e-8

# Discrétisation du temps

T=np.linspace(0,10,250)

## Résolution avec utilisation du module python ODEint ##

w0=[x1,y1,x2,y2]

wsol=odeint(effet,w0,T,atol=xlim,rtol=ylim)
X=[wsol[i][0] for i in range(250)]
Y=[wsol[i][2] for i in range(250)]

omega=15
C=0.5*(Cs*rho*A*omega*r)/m
wsol1=odeint(effet,w0,T,atol=xlim,rtol=ylim)
X1=[wsol1[i][0] for i in range(250)]
Y1=[wsol1[i][2] for i in range(250)]

omega=25
C=0.5*(Cs*rho*A*omega*r)/m
wsol2=odeint(effet,w0,T,atol=xlim,rtol=ylim)
X2=[wsol2[i][0] for i in range(250)]
Y2=[wsol2[i][2] for i in range(250)]

omega=10
C=0.5*(Cs*rho*A*omega*r)/m
wsol1=odeint(effet,w0,T,atol=xlim,rtol=ylim)
X3=[wsol1[i][0] for i in range(250)]
Y3=[wsol1[i][2] for i in range(250)]

omega=20
C=0.5*(Cs*rho*A*omega*r)/m
wsol1=odeint(effet,w0,T,atol=xlim,rtol=ylim)
X4=[wsol1[i][0] for i in range(250)]
Y4=[wsol1[i][2] for i in range(250)]

## Tracé des solutions ##

plt.plot(X,Y,label='5 rad.s-1')
plt.plot(X3,Y3,label='10 rad.s-1')
plt.plot(X1,Y1,label='15 rad.s-1')
plt.plot(X4,Y4,label='20 rad.s-1')
plt.plot(X2,Y2,label='25 rad.s-1')
plt.ylim(0,10)
plt.xlim(-2,2)
plt.grid()
plt.title('Trajectoires avec plusieurs vitesses angulaires')
plt.legend(loc='best')
plt.xlabel('x (en m)')
plt.ylabel('y (en m)')
plt.show()

