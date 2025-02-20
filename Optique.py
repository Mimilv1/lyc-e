# Créé par emilien, le 02/09/2022 en Python 3.7
import numpy as np
import matplotlib.pyplot as plt
n=1.5
R=1
x1=-0.5
x2=4

def xl(yl):
    return np.sqrt(R**2-yl**2)

def i(yl):
    return np.arcsin(yl/R)

yMax=R/n

def r(yl):
    if abs(yl)>yMax:
        return None
    else:
        return np.arcsin(n*np.sin(i(yl)))

def D(yl):
    if abs(yl)>yMax:
        return None
    else:
        return r(yl)-i(yl)

def y2(yl):
    if abs(yl)>yMax:
        return None
    else:
        return yl-np.tan(D(yl))*(x2-xl(yl))

plt.plot([0,0],[-R,R],color='black')
yS = np.linspace(-R,R,500)
plt.plot(xl(yS),yS,color='black')
m=20
for yl in [k*R/m for k in range(-m,m+1)]:
    plt.plot([x1,xl(yl),x2],[yl,yl,y2(yl)], color='black')
plt.axis('scaled')
plt.show()