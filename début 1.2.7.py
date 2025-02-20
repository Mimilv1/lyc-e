from tkinter import *
from math import *
from PIL import Image, ImageTk
import time

l=1000
h=600
a,b,c,d=l-(l*0.057),h-(h*0.1),pi,7
liste_variable=[a,b,c,d]#x ballon ,y ballon , x ballon 2,y ballon 2,angle ballon ,vitesse ballon au début
vballon=liste_variable#x ballon ,y ballon , x ballon 2,y ballon 2,angle ballon ,vitesse ballon
sauvegarde=[a,b,c,d]

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
    boutonquitter=Button(fenetre, text="quitter", font=("courrier",25), bg="#FF00FF", fg='white',command=fenetre.quit)
    boutonquitter.pack(side=BOTTOM)#sert a incruté le bouton dans la fenetre "fenetre"
    boutoncreparit=Button(fenetre, text="relancer", font=("courrier",25), bg="#FF00FF", fg='white',command=c_repartit)
    boutoncreparit.pack(side=BOTTOM)
    bouton_plus_vitesse=Button(fenetre, text="+ de vitesse de base", font=("courrier",25), bg="#FF6600", fg='white',command=on_change_vitesse_plus)
    bouton_plus_vitesse.pack(side=BOTTOM)
    bouton_moins_vitesse=Button(fenetre, text="- de vitesse de base", font=("courrier",25), bg="#FF6600", fg='white',command=on_change_vitesse_moins)
    bouton_moins_vitesse.pack(side=BOTTOM)
    bouton_plus_angle=Button(fenetre, text="plus grand angle de base", font=("courrier",25), bg="#009595", fg='white',command=on_change_angle_plus)
    bouton_plus_angle.pack(side=BOTTOM)
    bouton_moins_angle=Button(fenetre, text="plus petit angle de base", font=("courrier",25), bg="#009595", fg='white',command=on_change_angle_moins)
    bouton_moins_angle.pack(side=BOTTOM)

def on_change_vitesse_plus():
    sauvegarde[3]=sauvegarde[3]+0.1

def on_change_vitesse_moins():
    if sauvegarde[3]-0.1!=0:
        sauvegarde[3]=sauvegarde[3]-0.1
    else:
        print("vitesse négative non accepté")

def on_change_angle_plus():
    sauvegarde[2]=sauvegarde[2]+pi/100

def on_change_angle_moins():
    sauvegarde[2]=sauvegarde[2]-pi/100

def trajectoire():
    dessin.create_arc((-(l/14)),(h/5),(l-(l/18)),(h+(h/2)),fill="grey",extent=127,style='arc',dash=(1,1))#dash permet de faire les pointillé

def changement_état():
    if vballon[2]>0:
        vballon[2]=vballon[2]-0.01
    else :
        vballon[2]=vballon[2]+0.01
    if vballon[2]>pi/2:
        vballon[3]=vballon[3]-vballon[2]*0.01
    else :
        vballon[3]=vballon[3]+0.003*vballon[3]+0.01

def c_repartit():
    xballon,yballon=dessin.coords(ballon)
    dessin.move(ballon,(liste_variable[0]-xballon),(liste_variable[1]-yballon))
    for i in range(4):
        liste_variable[i]=sauvegarde[i]
        vballon[i]=sauvegarde[i]

def sol_touché():
    pass

def pannier_touché():
    pass

trajectoire()
image = Image.open("balllon.png")
image = image.resize((round(h/4),round(h/4))) #(height, width)
monimage = ImageTk.PhotoImage(image)#transorler l'image en format qui peut être lut par tk
ballon = dessin.create_image(vballon[0],vballon[1],image=monimage)#dessin du ballon
lesboutons()
pannier(l,h)
fenetre.attributes('-topmost',True)#met au premier plan

while vballon[3]!=0:
    dessin.move(ballon,-((vballon[3])*sin(vballon[2])),vballon[3]*cos(vballon[2]))
    changement_état()
    time.sleep(0.01)
    dessin.update()

fenetre.mainloop()