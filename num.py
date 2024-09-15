import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N.
N = 1000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recover rate, gamma, (in 1/days).
beta, gamma = 0.2, 1./10
# A grid of timme points (in days)
t = np.linspace(0, 160, 160)

print(N, I0, R0, S0, beta, gamma, t)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

print(y0, ret, S, I, R)

# Plot the data on three separate curves for S(t), I(t) and R(t)
# TODO

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S/1000, 'b', alpha=0.5, lw=1, label='Susceptible')
ax.plot(t, I/1000, 'b', alpha=0.5, lw=1, label='Infectd')
ax.plot(t, R/1000, 'b', alpha=0.5, lw=1, label='Recovered with immunity')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0,1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()


## Implicita metoder

from scipy.optimize import fsolve

def oderhs(t,y):
    yt = t - 1000*y**3 # definiera f(t,y)
    return yt

h = 0.1
y0 = 1
t = 0.1

g = lambda y: y - h*oderhs(t,y) - y0 # definiera g(y)
y = fsolve(g,y0) # iterativ lösare

print("We're printing y ->", y)

import math as m

a = np.array([[1, 2, 3],
            [4, 5, 6]])
print(a)
