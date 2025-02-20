# Créé par emili, le 02/06/2021 en Python 3.7
u0=125
r=2**(1/12)
tableau_fréquence=[round(u0*r**i,2) for i in range(25)]
print("tableau des fréquence de 125Hz à 500Hz")
print(tableau_fréquence)

notes=["do","do#reb","ré","ré#mib","mi","fa","fa#solb","sol","sol#lab","la","la#sib","si"]
print("")
print("dictionnaire des fréquence de 125Hz à 500Hz")
dictionnaire={"do":(125,250,500)}
liste_de_tuple=[(tableau_fréquence[i],tableau_fréquence[i+12]) for i in range(len(notes))] # création de tuple de 2 valeur pour chaque fréquence
for i in range(1,len(notes)): # de 1 a len de notes pour ne pas prendre do qui a 3 valeur
    dictionnaire[notes[i]]=liste_de_tuple[i]# association des notes a leurs tuples
print(dictionnaire)