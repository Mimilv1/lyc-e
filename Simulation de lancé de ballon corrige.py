# Créé par Elève, le 31/03/2021 en Python 3.7
from tkinter import *
from math import *
from PIL import Image, ImageTk
import time


longeur = int(input("Longeur de la simulation en pixel"))
hauteur = int(input("Hauteur de la simulation en pixel"))
liste_variable = [longeur - (longeur * 0.057), hauteur - (hauteur * 0.1), pi, 7, 0, True, False, 0, 15]
# x ballon ,y ballon , x ballon 2,y ballon 2,angle ballon ,vitesse ballon au début,compteur pour attendre en miliseconde
# pour créer trajectoire,bool de si false stope la boucle,bool de pannier mis récemment, nb pannier
vballon = liste_variable  # x ballon ,y ballon , x ballon 2,y ballon 2,angle ballon ,vitesse ballon
sauvegarde = [longeur - (longeur * 0.057), hauteur - (hauteur * 0.1), pi, 7]
vecteur = [0., 0.]
impacte_recente = [0]

fenetre = Tk()
fenetre.title("Simulation")  # titre de la fenetre
fenetre.minsize(960, 720)  # taille minimum
fenetre.iconbitmap("icone.ico")  # changer l'icône
dessin = Canvas(fenetre, bg="grey", width=longeur, height=hauteur, bd=0, highlightthickness=0)
# canvas = espace dédié à la création graphique
dessin.pack(side=LEFT)  # sert à incruster dessin sur fenetre


def chiffres():
    global vitesse_a_modifier, angle_a_modifier, nbpannier_a_modifier

    vitesse_a_modifier = DoubleVar()  # Float
    label = Label(fenetre, textvariable=vitesse_a_modifier)
    label.pack()

    angle_a_modifier = DoubleVar()  # Float
    label2 = Label(fenetre, textvariable=angle_a_modifier)
    label2.pack()

    nbpannier_a_modifier = IntVar()  # Int
    label3 = Label(fenetre, textvariable=nbpannier_a_modifier)
    label3.pack()


def pannier(long, haut):
    dessin.create_line((long / 20), haut, (long / 20), (haut / 9), fill="#000000", width=5)
    dessin.create_line((long / 20), (haut / 3), (long / 5), (haut / 3), fill="#000000", width=5)
    dessin.create_line((long / 20), (haut / 3), (long / 11), (haut / 2.1), fill="#000000")
    dessin.create_line((long / 5), (haut / 3), (long / 6), (haut / 2.1), fill="#000000")
    dessin.create_arc((long / 6), (haut / 2.15), (long / 11), (haut / 2.05), fill="grey", style='arc', extent=180)
    # style sert à retirer les  rayons
    dessin.create_arc((long / 6), (haut / 2.15), (long / 11), (haut / 2.05), fill="grey", style='arc', extent=-180)
    # extent : angle entre les deux points


def lesboutons():
    boutonquitter = Button(fenetre, text="quitter", font=("courrier", 25), bg="#FF00FF", fg='white', command=quitter)
    boutonquitter.pack(side=BOTTOM)  # sert à incruter le bouton dans la fenêtre "fenetre"

    boutoncreparit = Button(fenetre, text="relancer", font=("courrier", 25), bg="#FF00FF", fg='white',
                            command=c_repartit)
    boutoncreparit.pack(side=BOTTOM)

    bouton_plus_vitesse = Button(fenetre, text="+ de vitesse de base", font=("courrier", 25), bg="#FF6600", fg='white',
                                 command=on_change_vitesse_plus)
    bouton_plus_vitesse.pack(side=BOTTOM)

    bouton_moins_vitesse = Button(fenetre, text="- de vitesse de base", font=("courrier", 25), bg="#FF6600", fg='white',
                                  command=on_change_vitesse_moins)
    bouton_moins_vitesse.pack(side=BOTTOM)

    bouton_plus_angle = Button(fenetre, text="plus grand angle de base", font=("courrier", 25), bg="#00BBBB",
                               fg='white', command=on_change_angle_plus)
    bouton_plus_angle.pack(side=BOTTOM)

    bouton_moins_angle = Button(fenetre, text="plus petit angle de base", font=("courrier", 25), bg="#00BBBB",
                                fg='white', command=on_change_angle_moins)
    bouton_moins_angle.pack(side=BOTTOM)


def on_change_vitesse_plus():
    sauvegarde[3] = sauvegarde[3] + 0.1


def on_change_vitesse_moins():
    if sauvegarde[3] - 0.1 > 0:
        sauvegarde[3] = sauvegarde[3] - 0.1


def quitter():
    fenetre.destroy()
    liste_variable[5] = False  # permet de quitter la boucle while sans erreur car dessin n'existe plus


def on_change_angle_plus():
    sauvegarde[2] = sauvegarde[2] + pi / 100


def on_change_angle_moins():
    sauvegarde[2] = sauvegarde[2] - pi / 100


def trajectoire(frequence):
    if liste_variable[4] == frequence:
        # plus le chiffre est petit (1 le plus petit) plus la simulation sera ralenti par les lags
        xballon, yballon = dessin.coords(ballon)
        dessin.create_rectangle(xballon, yballon, xballon, yballon, fill="#000000")
        liste_variable[4] = 0
    liste_variable[4] += 1


def changement_etat():
    xballon, yballon = dessin.coords(ballon)
    angle = (vballon[2] * 180) / pi

    # vballon[2] est l'angle en radian vballon[3] est la vitesse en pixel par miliseconde
    if angle > 360:  # test de si l'angle est trop grand
        vballon[2] = vballon[2] - ((angle // 360) * 2 * pi)
        angle = (vballon[2] * 180) / pi
    if round(angle) < 0:  # test de si l'angle est trop petit
        angle = (angle + ((angle // -360) * 360)) + 360
        vballon[2] = ((angle / 180) * pi)
        angle = (vballon[2] * 180) / pi

    vecteur[0] = vballon[3] * (-sin(vballon[2]))  # déplacement x
    vecteur[1] = vballon[3] * (cos(vballon[2]))  # déplacement y

    if 360 > angle > 180:  # test dans quelle situation d'angle on est
        vballon[2] = vballon[2] + 0.005 + (cos(vballon[2]) / cos(vballon[2])) * 0.005
    elif angle != 0 and angle != 180:
        vballon[2] = vballon[2] - 0.005 - (cos(vballon[2]) / cos(vballon[2])) * 0.005
    if 360 > round(angle) > 270 or 90 > round(angle) > 0:
        # changement d'état en fonction de l'angle (changement de l'angle et la vitesse)
        vballon[3] = vballon[3] + vballon[3] * 0.01
    elif angle != 0 and angle != 180:
        vballon[3] = vballon[3] - vballon[3] * 0.01
    if round(angle) == 180 and round(yballon) < (hauteur - (hauteur / 10) - 0.03):
        # test de si le ballon a une trajctiore verticale et test de sile ballon n'est pas au sol
        vballon[3] = vballon[3] - 0.03
        if (round(vballon[3]*10)/10) == 0:  # test de si la vitesse est égalle à 0 pour changer l'angle
            vballon[2] = 0
            vecteur[1] = vballon[3] * (sin(vballon[2]))
    elif round(angle) == 0:  # test de si l'angle est égalle a 0
        vballon[3] = vballon[3] + 0.03
        vballon[2] = 0
    if impacte_recente[0] != 0:
        impacte_recente[0] = impacte_recente[0] - 1


def c_repartit():
    xballon, yballon = dessin.coords(ballon)
    dessin.move(ballon, (liste_variable[0] - xballon), (liste_variable[1] - yballon))
    # déplacement du ballon au point de départ
    vecteur[0] = 0
    vecteur[1] = 0
    liste_variable[6] = False  # pannier récent = False
    for i in range(4):
        liste_variable[i] = sauvegarde[i]
        vballon[i] = sauvegarde[i]


def impact():
    if (vballon[3] * 0.8) - 0.3 > 0:
        vballon[3] = (vballon[3] * 0.8) - 0.3
    else:
        vballon[3] = 0
    impacte_recente[0] = 4


def sol_touche():
    xballon, yballon = dessin.coords(ballon)
    if round(yballon) > (hauteur - (hauteur / 10)):  # hitbox du sol
        if vballon[2] > pi and impacte_recente[0] == 0:
            vballon[2] = 2 * pi - (vballon[2] - pi)
            impact()
        elif vballon[2] == 0 and impacte_recente[0] == 0:
            vballon[2] = pi
            impact()
        elif vballon[2] < pi and impacte_recente[0] == 0:
            vballon[2] = pi - vballon[2]
            impact()


def pannier_touche():
    xballon, yballon = dessin.coords(ballon)
    if (round(longeur / 20) + hauteur / 10) > round(xballon) > round(longeur / 21) \
            and round(yballon) > round(hauteur / 9):
        if vballon[2] > (pi / 2):
            vballon[2] = (3 * pi / 2) - (vballon[2])
        vballon[2] = ((pi / 2 + vballon[2]) + pi - vballon[2])
        impact()


def compteur_nb_pannier():
    xballon, yballon = dessin.coords(ballon)
    if (longeur / 20) < xballon < (longeur / 5) and ((hauteur / 3) + 10) > yballon > ((hauteur / 3) - 10) and\
            not(liste_variable[6]):
        liste_variable[7] += 1  # compteur de pannier
        liste_variable[6] = True  # variable pannier récent a true


def affichage_vitesse_angle_nbpannier():
    vitesse_a_modifier.set(vballon[3])
    angle_a_modifier.set(vballon[2])
    compteur_nb_pannier()
    nbpannier_a_modifier.set(liste_variable[7])


def anti_lag(frequence):
    # sert a ne pas update trop souvent le compteur de vitesse et d'angle qui ralentissait beaucoup le programme
    if liste_variable[8] >= frequence:
        affichage_vitesse_angle_nbpannier()
        liste_variable[8] = 0
    else:
        liste_variable[8] += 1


image = Image.open("balllon.png")
image = image.resize((round(hauteur / 4), round(hauteur / 4)))  # (height, width)
monimage = ImageTk.PhotoImage(image)  # transformer l'image en format qui peut être lu par tk
ballon = dessin.create_image(vballon[0], vballon[1], image=monimage)  # dessin du ballon
lesboutons()
pannier(longeur, hauteur)
chiffres()
fenetre.attributes('-topmost', True)  # met au premier plan


def moteur():
    while liste_variable[5]:
        # on vérifie si il faut casser la boucle si l'utilisateur aurait appuyer sur le bouton quitter
        dessin.move(ballon, vecteur[0], vecteur[1])  # on bouge la ballon
        pannier_touche()  # on test si le pannier a été toucher
        sol_touche()  # on test si le sol a été toucher
        changement_etat()  # on change la vitesse et l'angle du ballon
        trajectoire(15)  # on met un point noir sur la position du ballon
        anti_lag(15)  # affichage de la vitesse et l'angle actuelle du ballon
        dessin.update()  # on update le canva
        time.sleep(0.01)  # on attend 0.01s


moteur()
fenetre.mainloop()
