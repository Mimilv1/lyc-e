
cartej1=input()
cartej2=input()
compteur=0
victoire=0
i=0
if len(cartej1)>len(cartej2):
   while i!=len(cartej2)-1 and victoire!=1:
      if cartej1[i]>cartej2[i]:
         print("2")
         print(compteur)
         victoire=1
      elif cartej1[i]<cartej2[i]:
         print("1")
         print(compteur)
         victoire=1
      i=+1
      compteur=+1
   if victoire!=1:
      print("1")
      print(compteur)
elif len(cartej1)==len(cartej2):
   while i!=len(cartej2)-1 or victoire!=1:
      if cartej1[i]>cartej2[i]:
         print("2")
         print(compteur)
      elif cartej1[i]<cartej2[i]:
         print("1")
         print(compteur)
         victoire=1
      compteur=+1
      i=+1
   if victoire!=1:
      print("=")
else:
   while i!=len(cartej1)-1 and victoire!=1:
      if cartej1[i]>cartej2[i]:
         print("2")
         print(compteur)
         victoire=1
      elif cartej1[i]<cartej2[i]:
         print("1")
         print(compteur)
         victoire=1
      compteur=+1
      i=+1
   if victoire!=1:
      print("2")
      print(compteur)

