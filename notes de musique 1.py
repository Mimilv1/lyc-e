# Créé par emili, le 02/06/2021 en Python 3.7
u0=125
r=2**(1/12)
t=[round(u0*r**i,2) for i in range(25)]
print("tableau des fréquence de 125Hz à 500Hz")
print(t)

notes=["do","do#reb","ré","ré#mib","mi","fa","fa#solb","sol","sol#lab","la","la#sib","si"]

print("")
print("dictionnaire des fréquence de 125Hz à 500Hz")
dictionnaire2={"do":(125,250,500)}
liste2=[(t[i],t[i+12]) for i in range(len(notes))]
for i in range(1,len(notes)):
    dictionnaire2[notes[i]]=liste2[i]
print(dictionnaire2)