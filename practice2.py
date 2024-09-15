## 2)
## my''(t)+cy'(t)+ky(t)=0 -> y''(t)=(-cy'(t)-k*y(t))/m
## skriv om på formen 
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def ODE_fun(t, u, m,k,c):
    u1, u2 = u
    u = [u2, (-c*u2 - k*u1)/m]
    return u

u0 = np.array([0,1]) # y(0) resp. y´(0)
tspan = [0, 2]
m = 2
k = 100
c = 0.1
eval = np.arange(tspan[0], tspan[1], 0.01)
result = solve_ivp(ODE_fun, tspan, u0, t_eval=eval, args=(m,k,c))
