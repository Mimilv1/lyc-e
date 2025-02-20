import numpy as np
import matplotlib.pyplot as plt
import spicy as sp



def f(t):
    if (t%(2*np.pi))<np.pi:
        return t%(2*np.pi)
    else:
        return 2*np.pi-(t%(2*np.pi))


X = np.arange(-4*np.pi, 4 * np.pi, 0.01)
Y = list(map(f, X))
plt.plot(X,Y)
plt.show()

def g(f,t):
    return f(t)*np.cos(t)

def r(f,t):
    return f(t)*np.sin(t)

def coef(f, n):
    la = []
    lb = []
    o = lambda x : g(f, x)
    m = lambda x : r(f, x)
    for i in range(n+1):
        la.append(1/(np.pi) * sp.integrate.quad(o,0, 2*np.pi))
        lb.append(1/(np.pi) * sp.integrate.quad(m,0, 2*np.pi))
    return la, lb

def SN(n,f,x):