from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import spicy.optimize as resol

def LL(d):
    ListeListes = [[1]]
    for k in range(d):
        ListeNouveau = []
        for L in ListeListes:
            ListeNouveau.append(L+[0])
            ListeNouveau.append(L+[1])
            ListeListes = ListeNouveau
    for L in ListeListes:
        L.append(1)
    return ListeListes


color =["green", "red", "orange", "purple", 'blue', "black", "grey"]

print(LL(1))
LesW = [set() for i in range(7)]

for i in range(7):
    for j in LL(i):
        for t in Polynomial(j).roots():
            LesW[i].add(t)

    plt.scatter([k.real for k in LesW[i]], [k.imag for k in LesW[i]], color=color[i])


def module(z):
    return (z.real**2 + z.imag**2)**0.5


def f(z):
    return module(z)/(1-module(z))


def g(z):
    return module((2*z-1)/(z-1))


print(resol.fsolve(f,g))

plt.show()
