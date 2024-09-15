## 1) 
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def ODE_fun(t, y):
    yprime = np.sin(y*t)
    return yprime

y0 = [1]
tspan = [0, 5]
eval = np.arange(tspan[0], tspan[1], 0.01)
result = solve_ivp(ODE_fun, tspan, y0, t_eval = eval)

plt.plot(result.t, result.y[0])
plt.show()

