# Créé par emili, le 11/05/2021 en Python 3.7
t_nombres=[1,2,3,5,6,7,10,11,12,16,18,21,22,23,24,30,81]

def trouvé_le(t_nombres,nombre_recherché):
    indice_milieu=len(t_nombres)//2
    if t_nombres[indice_milieu]==nombre_recherché:
        if len(t_nombres)%2==0:
            return indice_milieu
        else:
            return indice_milieu+1
    elif t_nombres[indice_milieu]<nombre_recherché:
        for i in range(len(t_nombres)//2,len(t_nombres)):
            if t_nombres[i]==nombre_recherché :
                return i
    else:
        for i in range(0,len(t_nombres)//2):
            if t_nombres[i]==nombre_recherché :
                return i

for i in range(len(t_nombres)):
    print(trouvé_le(t_nombres,t_nombres[i]))