# Créé par Elève, le 31/03/2021 en Python 3.7
from tkinter import *
from math import *
from PIL import Image, ImageTk
import time

l=1000#int(input("Longeur de la simulation en pixel"))
h=600#int(input("hauteur de la simulation en pixel"))
liste_variable=[l-(l*0.057),h-(h*0.1),pi,7,0,False,False,0]#x ballon ,y ballon , x ballon 2,y ballon 2,angle ballon ,vitesse ballon au début,compteur pour attendre en miliseconde pour créer trajectoire,bool de si true stope la boucle,bool de pannier mis réssament, nb pannier
vballon=liste_variable#x ballon ,y ballon , x ballon 2,y ballon 2,angle ballon ,vitesse ballon
sauvegarde=[l-(l*0.057),h-(h*0.1),pi,7]
vecteur=[0,0]
impacte_récente=[0]

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

    boutonquitter=Button(fenetre, text="quitter", font=("courrier",25), bg="#FF00FF", fg='white',command=quitter)
    boutonquitter.pack(side=BOTTOM)#sert a incruté le bouton dans la fenetre "fenetre"

    boutoncreparit=Button(fenetre, text="relancer", font=("courrier",25), bg="#FF00FF", fg='white',command=c_repartit)
    boutoncreparit.pack(side=BOTTOM)

    bouton_plus_vitesse=Button(fenetre, text="+ de vitesse de base", font=("courrier",25), bg="#FF6600", fg='white',command=on_change_vitesse_plus)
    bouton_plus_vitesse.pack(side=BOTTOM)

    bouton_moins_vitesse=Button(fenetre, text="- de vitesse de base", font=("courrier",25), bg="#FF6600", fg='white',command=on_change_vitesse_moins)
    bouton_moins_vitesse.pack(side=BOTTOM)

    bouton_plus_angle=Button(fenetre, text="plus grand angle de base", font=("courrier",25), bg="#00BBBB", fg='white',command=on_change_angle_plus)
    bouton_plus_angle.pack(side=BOTTOM)

    bouton_moins_angle=Button(fenetre, text="plus petit angle de base", font=("courrier",25), bg="#00BBBB", fg='white',command=on_change_angle_moins)
    bouton_moins_angle.pack(side=BOTTOM)

def on_change_vitesse_plus():
    sauvegarde[3]=sauvegarde[3]+0.1

def on_change_vitesse_moins():
    if sauvegarde[3]-0.1>0:
        sauvegarde[3]=sauvegarde[3]-0.1
    else:
        print("vitesse négative non accepté")

def quitter():
    fenetre.destroy()
    liste_variable[5]=True #permet de quitter la boucle while sans erreur car dessin n'existe plus

def on_change_angle_plus():
    sauvegarde[2]=sauvegarde[2]+pi/100

def on_change_angle_moins():
    sauvegarde[2]=sauvegarde[2]-pi/100

def trajectoire():
    if liste_variable[4]==8: # plus le chiffre est petit (1) le plus petit plus la simulation serat ralentit par les lag
        xballon,yballon=dessin.coords(ballon)
        dessin.create_rectangle(xballon,yballon,xballon,yballon,fill="#000000")
        liste_variable[4]=0
    liste_variable[4]+=1

def changement_état():
    angle=(vballon[2]*180)/pi
    if angle>360 : # test de si l'angle est trop grand
        vballon[2]=vballon[2]-((angle//360)*2*pi)
        angle=(vballon[2]*180)/pi
    if round(angle)<0: # test de si l'angle est trop petit
        angle=(angle+((angle//-360)*360))+360
        vballon[2]=((angle/180)*pi)
        angle=(vballon[2]*180)/pi
    angle_rad=vballon[2]
    vitesse=vballon[3]
    vitesse_pos=abs(vitesse)
    v0=vitesse_pos
    vecteur[0]=v0*(-sin(angle_rad))
    vecteur[1]=v0*(cos(angle_rad))
    if angle<360 and angle>=270:
        vballon[2]=vballon[2]+0.005+(cos(angle_rad)/cos(angle_rad))*0.005
        vballon[3]=vballon[3]+vballon[3]*0.01
    elif angle<270 and angle>180:
        vballon[2]=vballon[2]+0.005+(cos(angle_rad)/cos(angle_rad))*0.005
        vballon[3]=vballon[3]-vballon[3]*0.01
    elif angle<180 and angle>90:
        vballon[2]=vballon[2]-0.005-(cos(angle_rad)/cos(angle_rad))*0.005# différence de trajectoire sur un même lancer a cause d'adition de float
        vballon[3]=vballon[3]-vballon[3]*0.01
    elif angle<=90 and round(angle)>0:
        vballon[2]=vballon[2]-0.005-(cos(angle_rad)/cos(angle_rad))*0.005
        vballon[3]=vballon[3]+vballon[3]*0.01
    elif round(angle)==180: # test de si le ballon a une trajctiore verticale
        vballon[3]=vballon[3]-0.03
        if (round(vballon[3]*10))/10==0: # test de si la vitesse est égalle à 0 pour changer l'angle
            vballon[2]=0
            angle_rad=vballon[2]
            vecteur[1]=v0*(sin(angle_rad))
    elif round(angle)==0: # test de si l'nagle est égalle a 0
        vballon[3]=vballon[3]+0.03
        vballon[2]=0
        angle_rad=vballon[2]
        angle=0
    if impacte_récente[0]!=0:
        impacte_récente[0]=impacte_récente[0]-1

def c_repartit():

    xballon,yballon=dessin.coords(ballon)
    dessin.move(ballon,(liste_variable[0]-xballon),(liste_variable[1]-yballon))
    vecteur[0]=0
    vecteur[1]=0

    for i in range(4):
        liste_variable[i]=sauvegarde[i]
        vballon[i]=sauvegarde[i]

def impact():
    if (vballon[3]*0.8)-0.3>0:
        vballon[3]=(vballon[3]*0.8)-0.3
    else:
        vballon[3]=0
    impacte_récente[0]=4

def sol_touché():
    xballon,yballon=dessin.coords(ballon)
    print(vballon[3])
    if round(yballon)>(h-(h/10)):
        if vballon[2]>pi and impacte_récente[0]==0:
            vballon[2]=2*pi-(vballon[2]-pi)
            impact()
        elif vballon[2]==0 and impacte_récente[0]==0:
            vballon[2]=pi
            impact()
        elif vballon[2]<pi and impacte_récente[0]==0:
            vballon[2]=pi-vballon[2]
            impact()

def pannier_touché():
    xballon,yballon=dessin.coords(ballon)
    if round(xballon)<(round(l/20)+h/10) and round(yballon)>round(h/9) and round(xballon)>round(l/21):
        if vballon[2]>(pi/2):
            vballon[2]=(3*pi/2)-(vballon[2])
        vballon[2]=((pi/2+vballon[2])+pi-vballon[2])
        impact()

def affichage_vitesse_angle_nbpannier():
    pass

def compteur_nb_pannier():
    xballon,yballon=dessin.coords(ballon)
    if xballon and yballon and pannier_récent==False:
        liste_variable[7]+=1
        pannier_récent=True

image = Image.open("balllon.png")
image = image.resize((round(h/4),round(h/4))) #(height, width)
monimage = ImageTk.PhotoImage(image)#transorler l'image en format qui peut être lut par tk
ballon = dessin.create_image(vballon[0],vballon[1],image=monimage)#dessin du ballon
lesboutons()
pannier(l,h)
fenetre.attributes('-topmost',True)#met au premier plan

while True:
    dessin.move(ballon, vecteur[0],vecteur[1])
    pannier_touché()
    sol_touché()
    changement_état()
    trajectoire()
    dessin.update()
    time.sleep(0.001)
    if liste_variable[5]==True:
        break

fenetre.mainloop()
