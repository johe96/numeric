# NumPy for numerical operations
import numpy as np
# solve_ivp from SciPy for solving initial value problems
from scipy.integrate import solve_ivp
# fsolve from scipy for finding roots of equations (not used in this snippet) 
from scipy.optimize import fsolve
# Matplotlib for plotting
import matplotlib.pyplot as plt

# Problem 1
# ODE definition

# this defines the ordinary differential equation (ODE) you're
# solving: dy/dy = -y + sin(t)
def ode1(t,y):
    yder=-y+np.sin(t)
    return yder



# Sets the time span from 0 to 10 
# Sets the initial condition y(0) = 0
tspan=[0, 10]; y0=[0]
# Evaluera i tpunkter annars hackig kurva
# Creates 101 evenly spaced points between 0 and 10 for evaluation
tpunkter=np.linspace(tspan[0],tspan[1], 101)
# Solving the ODE
sol = solve_ivp(ode1,tspan,y0,t_eval=tpunkter)
plt.plot(sol.t,sol.y[0],'-k')
plt.title('Uppgift 1, solve_ivp')
plt.show()

# Problem 2
def ode2(t,y):
    yder=np.zeros(2);
    yder[0]=y[1]
    yder[1]=-3*y[1]-2*y[0]
    return yder

tspan=[0, 10]
y0=[2, 1]
sol = solve_ivp(ode2,tspan,y0)
plt.plot(sol.t,sol.y[0],'r-')
plt.plot(sol.t,sol.y[1],'g-')
plt.title('Uppgift 2')
plt.legend(['y(t)', 'dy(t)/dt'])
plt.show()

# Problem 3 (klarar även system av ODEr)
def Heun(f,tspan,u0,dt):
    interval=round((tspan[1]-tspan[0])/dt)
    tvec=np.linspace(tspan[0],tspan[1],interval+1)
    u=np.zeros((len(tvec), len(u0)))
    i=0
    u[i,:]=u0
    for t in tvec[0:len(tvec)-1]:
        k1=f(t,u[i,:])
        k2=f(t+dt,u[i,:]+dt*k1)
        k=(k1+k2)/2
        u[i+1,:]=u[i,:]+dt*k
        i+=1
    return tvec, u

tspan=[0, 10]; y0=[0]; dt=0.1
t,y = Heun(ode1,tspan,y0,dt)
plt.plot(t,y,'-r')
plt.title('Uppgift 3, Heun')
plt.show()

# Problem 4
def EulerImplicit(f,tspan,u0,dt):
    interval=round((tspan[1]-tspan[0])/dt)
    tvec=np.linspace(tspan[0],tspan[1],interval+1)
    u=np.zeros(len(tvec))
    i=0
    u[i]=u0
    for t in tvec[0:len(tvec)-1]:
        fekv = lambda unew: unew-u[i]-dt*f(t+dt,unew)
        u[i+1]=fsolve(fekv,u[i])
        i+=1
    return tvec, u

tspan=[0, 10]; y0=0; dt=0.1
t,y = EulerImplicit(ode1,tspan,y0,dt)
plt.plot(t,y,'-b')
plt.title('Uppgift 4, Implicit Euler')
plt.show()
