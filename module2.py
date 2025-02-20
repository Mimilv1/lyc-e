# Créé par emili, le 07/02/2021 en Python 3.7
cartej1=input()
cartej2=input()
compteur=0
victoire=0
if len(cartej1)>len(cartej2):
   for i in range(len(cartej2)):
      if cartej1[i]>cartej2[i]:
         print("2")
         print(compteur)
         victoire=1
      elif cartej1[i]<cartej2[i]:
         print("1")
         print(compteur)
         victoire=1
      compteur=+1
   if victoire!=1:
      print("1")
      print(compteur)
elif len(cartej1)==len(cartej2):
   for i in range(len(cartej1)):
      if cartej1[i]>cartej2[i]:
         print(2)
         print(compteur)
      elif cartej1[i]<cartej2[i]:
         print("1")
         print(compteur)
         victoire=1
      compteur=+1
   if victoire!=1:
      print("=")
else:
   for i in range(len(cartej2)):
        if cartej1[i]>cartej2[i]:
            print("2")
            print(compteur)
            victoire=1
        elif cartej1[i]<cartej2[i]:
            print("1")
            print(compteur)
            victoire=1
        compteur=+1
   if victoire!=1:
      print("2")
      print(compteur)
