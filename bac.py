P=[8,5,2,4]
Test=[x**2 for x in range(9,-1,-1)]

def empiler(x,y):
    x.append(y)

def depiler(x):
    a=x[len(x)-1]
    x.__delitem__(len(x)-1)
    return a

def est_vide(x):
    return not(bool(len(x)))

def hauteur_pile(P):
    Q = []
    n = 0
    while not(est_vide(P)):
        n+=1
        x = depiler(P)
        empiler(Q,x)
    while not (est_vide(Q)):
        x=depiler(Q)
        empiler(P,x)
    return n

def max_pile(P,i):
    if i>hauteur_pile(P):
        i=hauteur_pile(P)
    if i==0:
        return None
    l=[0]*i
    for z in range(i):
        l[z]=depiler(P)
    maxi=max(l)
    for e in range(i-1,-1,-1):
        empiler(P,l[e])
    return maxi

def retourner(P,j):
    if j>hauteur_pile(P):
        j=hauteur_pile(P)
    Q=[]
    Z=[]
    for e in range(j):
        x = depiler(P)
        empiler(Q,x)
    for d in range(len(Q)):
        x = depiler(Q)
        empiler(Z,x)
    for d in range(len(Z)):
        x = depiler(Z)
        empiler(P,x)

def tri_crêpe(): # a finir
    pass