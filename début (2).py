from tkinter import *
from turtle import *
import time

l=int(input("Longeur d'écran en pixel"))
h=int(input("hauteur d'écran en pixel"))
fenetre= Tk()
#fenetre=turtle.getcanvas().fenetre
vballon=[l-(l*0.01),h-(h*0.01),l-(l*0.1),h-(h*0.16),1,1]#x ballon ,y ballon , x ballon 2,y ballon 2,angle ballon ,vitesse ballon

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
    dessin.create_arc((-(l/14)),(h/5),(l-(l/18)),(h+(h/2)),fill="grey",extent=127,style='arc',dash=(1,1))

trajectoire()
lesboutons()
pannier(l,h)

ballon = dessin.create_oval(vballon[0],vballon[1],vballon[2],vballon[3],fill="#FF8F00")#dessin du ballon
#dessin.delete(ballon) pour faire l'animation delete le ballon et le recréer avec les nouvelles coordonées
fenetre.lift()#met au premier plan
fenetre.attributes('-topmost',True)

fenetre.mainloop()