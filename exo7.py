import numpy.random as rd
import numpy as np
import matplotlib.pyplot as plt
global r
r = 10


def X():
    return rd.randint(1, r + 1)


def T(i):
    ensemble_Tr = set()
    valeur = 0
    k = 0
    while valeur < i:
        ensemble_Tr.add(X())
        valeur = len(ensemble_Tr)
        k=k+1
    return k


def P(Variable, i, k): # pour la Q1b
    iteration = 1000
    positif = 0
    for j in range(iteration):
        if Variable(k) == i:
            positif += 1
    return positif/iteration


def E(T):
    somme = 0
    for i in range(1,10*r):
        somme += i*P(T, i, r)
    return somme





def phi(t):
    iteration = 1000
    positif = 0
    for j in range(iteration):
        if r*np.log(r)+t*r>=T(r) >=r*np.log(r)-t*r:
            positif += 1
    return positif / iteration


def f(t):
    return np.exp(-np.exp(-t))-np.exp(-np.exp(t))

tab=np.arange(0,3, 0.01)

Y1 = [f(x) for x in tab]

Y2 = [phi(x) for x in tab]

plt.plot(tab,Y1)
plt.plot(tab,Y2)
plt.show()
