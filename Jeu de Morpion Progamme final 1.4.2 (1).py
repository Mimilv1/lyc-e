from tkinter import *
import time

A1, A2, A3, B1, B2, B3, C1, C2, C3, t=0, 0, 0, 0, 0, 0, 0, 0, 0, 0

# "t" c'est le nombre de tours qui permettent de calculer si le joueur 1 ou 2 a
# gagné (si le tour est pair, c'est le joueur 2, sinon, c'est le joueur 1.)
# Cela permet aussi de savoir si la partie est nulle, si le nombre de tours
# dépasse 9, la partie est nulle.

fenetre = Tk()

fenetre.title("Jeu de Morpion")

w = int(input("Choisissez la résolution: Largeur:"))
h = int(input("Choisissez la résolution: Hauteur:"))

dessin = Canvas(fenetre, bg = "white", width = w, height = h)

dessin.pack()

def coord(): #coordonnées graphiques

    dessin.create_text(((1/3)*w)/2, 10, text = "A", fill="black")
    dessin.create_text(w/2, 10, text = "B", fill="black")
    dessin.create_text(((2/3)*w)+(1/2)*((1/3)*w), 10, text = "C", fill="black")
    dessin.create_text(10, ((1/3)*h)/2, text = "1", fill="black")
    dessin.create_text(10, h/2, text = "2", fill="black")
    dessin.create_text(10, ((2/3)*h)+(1/2)*((1/3)*h), text = "3", fill="black")

def cadr(): #cadriage

    dessin.create_line(0, (1/3)*h, w, (1/3)*h, fill="#000000")
    dessin.create_line((1/3)*w, 0, (1/3)*w, h, fill="#000000")
    dessin.create_line(0, (2/3)*h, w, (2/3)*h, fill="#000000")
    dessin.create_line((2/3)*w, 0, (2/3)*w, h, fill="#000000")

def ovale(FO):
    if FO=="A1":
        dessin.create_oval(w/20,h/20,w/3,h/3, fill="#FFFFFF")

    elif FO=="B1":
        dessin.create_oval(w/1.5,h/20,w/3,h/3, fill="#FFFFFF")

    elif FO=="C1":
        dessin.create_oval(w/1.5,h/20,w,h/3, fill="#FFFFFF")

    elif FO=="A2":
        dessin.create_oval(w/20,h/1.5,w/3,h/3, fill="#FFFFFF")

    elif FO=="B2":
        dessin.create_oval(w/1.5,h/1.5,w/3,h/3, fill="#FFFFFF")

    elif FO=="C2":
        dessin.create_oval(w/1.5,h/1.5,w,h/3, fill="#FFFFFF")

    elif FO=="A3":
        dessin.create_oval(w/20,h/1.5,w/3,h, fill="#FFFFFF")

    elif FO=="B3":
        dessin.create_oval(w/1.5,h/1.5,w/3,h, fill="#FFFFFF")

    elif FO=="C3":
        dessin.create_oval(w/1.5,h/1.5,w,h, fill="#FFFFFF")


def croix(FC):
    if FC=="A1":
        dessin.create_line(w/20,h/20,w/3,h/3, fill="#000000")
        dessin.create_line(w/20,h/3,w/3,h/20, fill="#000000")

    elif FC=="B1":
        dessin.create_line(w/1.5,h/20,w/3,h/3, fill="#000000")
        dessin.create_line(w/1.5,h/3,w/3,h/20, fill="#000000")

    elif FC=="C1":
        dessin.create_line(w/1.5,h/20,w,h/3, fill="#000000")
        dessin.create_line(w/1.5,h/3,w,h/20, fill="#000000")

    elif FC=="A2":
        dessin.create_line(w/20,h/1.5,w/3,h/3, fill="#000000")
        dessin.create_line(w/3,h/1.5,w/20,h/3, fill="#000000")

    elif FC=="B2":
        dessin.create_line(w/1.5,h/1.5,w/3,h/3, fill="#000000")
        dessin.create_line(w/3,h/1.5,w/1.5,h/3, fill="#000000")

    elif FC=="C2":
        dessin.create_line(w/1.5,h/1.5,w,h/3, fill="#000000")
        dessin.create_line(w,h/1.5,w/1.5,h/3, fill="#000000")

    elif FC=="A3":
        dessin.create_line(w/20,h/1.5,w/3,h, fill="#000000")
        dessin.create_line(w/3,h/1.5,w/20,h, fill="#000000")

    elif FC=="B3":
        dessin.create_line(w/1.5,h/1.5,w/3,h, fill="#000000")
        dessin.create_line(w/3,h/1.5,w/1.5,h, fill="#000000")

    elif FC=="C3":
        dessin.create_line(w/1.5,h/1.5,w,h, fill="#000000")
        dessin.create_line(w,h/1.5,w/1.5,h, fill="#000000")


def alignement(): #Vérifie si la partie est gagnée ou pas

    if t >= 9:
        print('Egalité!')
        time.sleep(2)
        exit()
    elif A1==1 and A2==1 and A3==1:
        print('joueur 1 a gagné')
        return True

    elif A1==2 and A2==2 and A3==2:
        print("joueur 2 a gagné")
        return True

    elif B1==1 and B2==1 and B3==1:
        print("joueur 1 a gagné")
        return True

    elif B1==2 and B2==2 and B3==2:
        print("joueur 2 a gagné")
        return True

    elif C1==1 and C2==1 and C3==1:
        print("joueur 1 a gagné")
        return True

    elif C1==2 and C2==2 and C3==2:
        print("joueur 2 a gagné")
        return True

    elif A1==1 and B1==1 and C1==1:
        print("joueur 1 a gagné")
        return True

    elif A1==2 and B1==2 and C1==2:
        print("joueur 2 a gagné")
        return True

    elif A2==1 and B2==1 and C2==1:
        print("joueur 1 a gagné")
        return True

    elif A2==2 and B2==2 and C2==2:
        print("joueur 2 a gagné")
        return True

    elif A3==1 and B3==1 and C3==1:
        print("joueur 1 a gagné")
        return True

    elif A3==2 and B3==2 and C3==2:
        print("joueur 2 a gagné")
        return True

    elif A1==1 and B2==1 and C3==1:
        print("joueur 1 a gagné")
        return True

    elif A1==2 and B2==2 and C3==2:
        print("joueur 2 a gagné")
        time.sleep(2)
        exit()

    elif A3==1 and B2==1 and C1==1:
        print("joueur 1 a gagné")
        return True

    elif A3==2 and B2==2 and C1==2:
        print("joueur 2 a gagné")
        return True

def jeu(userInput): #Fonction coeur du jeu

    global t
    global A1
    global A2
    global A3
    global B1
    global B2
    global B3
    global C1
    global C2
    global C3

    if userInput == "A1":

        if A1 == 0:

            if (t % 2) == 0:

                ovale("A1")
                A1 = 2
                fenetre.update()


            else:

                croix ('A1')
                A1 = 1
                fenetre.update()

        else:

            print ("Déjà pris!")
            t = t - 1
            start()

    elif userInput == "A2":

        if A2 == 0:

            if (t % 2) == 0:

                ovale('A2')
                A2 = 2
                fenetre.update()

            else:

                croix ('A2')
                A2 = 1
                fenetre.update()
        else:

            print('Déjà pris!')
            t = t - 1
            start()

    elif userInput == "A3":

        if A3 == 0:

            if (t % 2) == 0:

                ovale("A3")
                A3 = 2
                fenetre.update()

            else:

                croix ("A3")
                A3 = 1
                fenetre.update()
        else:

            print("Déjà pris!")
            t = t - 1
            start()

    elif userInput == "B1":

        if B1 == 0:

            if (t % 2) == 0:

                ovale("B1")
                B1 = 2
                fenetre.update()

            else:

                croix ("B1")
                B1 = 1
                fenetre.update()
        else:

            print("Déjà pris!")
            t = t - 1
            start()

    elif userInput == "B2":

        if B2 == 0:

            if (t % 2) == 0:

                ovale("B2")
                B2 = 2
                fenetre.update()

            else:

                croix ('B2')
                B2 = 1
                fenetre.update()
        else:

            print("Déjà pris!")
            t = t - 1
            start()

    elif userInput == 'B3':

        if B3 == 0:

            if (t % 2) == 0:

                ovale("B3")
                B3 = 2
                fenetre.update()

            else:

                croix ('B3')
                B3 = 1
                fenetre.update()
        else:

            print("Déjà pris!")
            t = t - 1
            start()


    elif userInput == "C1":

        if C1 == 0:

            if (t%2) == 0:

                ovale("C1")
                C1 = 2
                fenetre.update()

            else:

                croix("C1")
                C1 = 1
                fenetre.update()
        else:

            print("Déjà pris!")
            t = t - 1
            start()

    elif userInput == "C2":

        if C2 == 0:

            if (t%2) == 0:

                ovale("C2")
                C2 = 2
                fenetre.update()

            else:

                croix("C2")
                C2 = 1
                fenetre.update()
        else:

            print("Déjà pris!")
            t = t - 1
            start()

    elif userInput == "C3":

        if C3 == 0:

            if (t%2) == 0:

                ovale('C3')
                C3 = 2
                fenetre.update()

            else:

                croix ("C3")
                C3 = 1
                fenetre.update()
        else:

            print("Déjà pris!")
            t = t - 1
            start()

    elif userInput == "surrender":
        if (t%2) == 0:
            print ('Joueur 1 a gagné!')
            time.sleep(2)
            exit()
        else:
            print ('Joueur 2 a gagné!')
            time.sleep(2)
            exit()

    else:
        print ("OOOOH C'EST PAS UNE COORDONNEE CA!")
        t = t - 1
        start()



def demande():
    global t
    fenetre.update()
    while alignement() != True:
        start()
def start():
    print ('tapez "surrender" pour vous rendre')
    global t
    while alignement() != True:
        userInput = str(input("Entrez les coordonnées de votre mouvement:"))
        t = t + 1
        jeu(userInput)
    time.sleep(2)
    exit()

cadr()
coord()
fenetre.lift()
fenetre.attributes('-topmost',True)
demande()
fenetre.mainloop()