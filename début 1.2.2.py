from tkinter import *
from PIL import Image
from PIL import ImageTk
import time

l=int(input("Longeur d'écran en pixel"))
h=int(input("hauteur d'écran en pixel"))
vballon=[l-(l*0.057),h-(h*0.1),1,1]#x ballon ,y ballon , x ballon 2,y ballon 2,angle ballon ,vitesse ballon

fenetre = Tk()
fenetre.title("Simulation")#titre de la fenetre
fenetre.minsize(960,720)#taille minimum
fenetre.iconbitmap("icone.ico")#changer l'icône
dessin = Canvas(fenetre, bg = "grey", width = l, height = h,bd=0,highlightthickness=0)# canvas = espace dédier a la création graphique
dessin.pack(side=LEFT)#sert a incrusté dessin sur fenetre

def pannier(l,h):
    dessin.create_line((l/20),h,(l/20),(h/9),fill="#000000",width=5)
    dessin.create_line((l/20),(h/3),(l/5),(h/3),fill="#000000",width=5)
    dessin.create_line((l/20),(h/3),(l/11),(h/2.1),fill="#000000")
    dessin.create_line((l/5),(h/3),(l/6),(h/2.1),fill="#000000")
    dessin.create_arc((l/6),(h/2.15),(l/11),(h/2.05),fill="grey",style='arc',extent=180)#style sert a retirer les  rayons
    dessin.create_arc((l/6),(h/2.15),(l/11),(h/2.05),fill="grey",style='arc',extent=-180)#extent angle entre les deux points

def lesboutons():
    boutonquitter=Button(fenetre, text="quitter", font=("courrier",25), bg="#164839", fg='white',command=fenetre.quit)
    boutonquitter.pack(side=BOTTOM)#sert a incruté le bouton dans la fenetre "fenetre"

def trajectoire():
    dessin.create_arc((-(l/14)),(h/5),(l-(l/18)),(h+(h/2)),fill="grey",extent=127,style='arc',dash=(1,1))#dash permet de faire les pointillé

trajectoire()

image = Image.open("balllon.png")
image = image.resize((round(h/4),round(h/4)), Image.ANTIALIAS) #(height, width)
monimage = ImageTk.PhotoImage(image)#transorler l'image en format qui peut être lut par tk
ballon = dessin.create_image(vballon[0],vballon[1],image=monimage)#dessin du ballon
lesboutons()
pannier(l,h)
fenetre.attributes('-topmost',True)#met au premier plan
for i in range(600):
    dessin.move(ballon,-1,-1)
    time.sleep(0.01)
    dessin.update()
fenetre.mainloop()