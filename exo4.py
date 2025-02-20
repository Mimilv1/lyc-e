import numpy as np
def c(u, n, a, b):
    card = 0
    for i in range(1,n+1):
        if b >= u(i)-np.floor(u(i)) >= a:
            card += 1
    return card


def u(x):
    return x**0.5

#conjecture pour tout n >= 1 sqrt(n)>=1

def v(x):
    return np.log(x)
def test(u):
    for i in range(1,500):
        print(c(u, i, 0, 1/2), end=" ")
    print()
#conjecture ln(1) dans 0 1/2
#et ln(n) pas dans 0 1/2

r = lambda x : (((1+5**0.5)/2))**x
test(u)
test(v)
test(r) # conjecture pas de nombre de cette suite dans 0,1/2

def somme(u,v):
    for i in range(1,10):
        print(u(i) + v(i))

def k(x):
    return ((1-(5)**0.5)/2)**x

somme(r,k)
print(5.9-int(5.9))