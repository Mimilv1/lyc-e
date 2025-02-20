# Créé par emili, le 29/06/2021 en Python 3.7
territoire = [1, 1, 1, 1, 0, 0, 2, 2, 2, 2]
emplacement = [0] * 10
victoire = [False, False]
tour = [0]
liste_faction = ["plante", "eau", "feu", "terre", "magie", "tenebre"]
faction_choisie = []
textes = ""
unitej1 = []
unitej2 = []
batimentj1 = []
batimentj2 = []
piochej1 = []
piochej2 = []
for i in range(len(liste_faction)):
    if i != len(liste_faction) - 1:
        textes = textes + str(liste_faction[i]) + ", "
    else:
        textes = textes + str(liste_faction[i]) + "."


class Carte:
    def __init__(self, nom, faction, description, equipe):
        self.nom = nom
        self.faction = faction
        self.description = description
        self.equipe = equipe


class CarteDAttaque(Carte):
    def __init__(self, attaque, nom, faction, description, equipe):
        super().__init__(nom, faction, description, equipe)
        self.attaque = attaque

    def attaquer(self, cible):
        cible.degat(self.attaque)


class CarteDUnite(Carte):
    def __init__(self, vie, attaque, attaque_recente, nom, faction, description, equipe):
        super().__init__(nom, faction, description, equipe)
        self.vie = vie
        self.attaque = attaque
        self.attaque_recente = attaque_recente

    def degat(self, damage):
        self.vie -= damage
        print("\033[95m {}\033[00m".format(
            str("il reste " + str(self.vie) + " point de vie à " + self.nom + " de " + self.faction)))
        self.mort()

    def attaquer(self, cible):
        cible.degat(self.attaque)

    def utilisation(self):
        compteur = 0
        if self.equipe == 1:
            for carte in unitej1:
                if carte.nom == self.nom:
                    print("\033[91m {}\033[00m".format("cette unité est déja sur le terrain"))
                    tour[0] -= 1
                else:
                    compteur += 1
            if compteur == len(unitej1):
                unitej1.append(self)
        else:
            for carte in unitej2:
                if carte.nom == self.nom:
                    print("\033[91m {}\033[00m".format("cette unité est déja sur le terrain"))
                    tour[0] -= 1
                else:
                    compteur += 1
            if compteur == len(unitej2):
                unitej2.append(self)

    def mort(self):
        if self.vie <= 0:
            if self.equipe == 1:
                unitej1.remove(self)
            else:
                unitej2.remove(self)
            print("\033[95m {}\033[00m".format(str(self.nom) + " de " + str(self.faction) + " est mort"))


class CarteDeTerritoire(Carte):
    def __init__(self, avance, nom, faction, description, equipe):
        super().__init__(nom, faction, description, equipe)
        self.avance = avance

    def utilisation(self):
        if self.equipe == 1:
            decallage = int(self.avance / 10)
            compteur = 0
            modifi = 0
            while modifi != decallage and compteur != 10:
                if territoire[compteur] != 1:
                    territoire[compteur] = 1
                    modifi += 1
                compteur += 1
        else:
            decallage = int(self.avance / 10)
            compteur = 9
            modifi = 0
            while modifi != decallage and compteur != -1:
                if territoire[compteur] != 2:
                    territoire[compteur] = 2
                    modifi += 1
                compteur -= 1
        for batiment in batimentj1:
            batiment.mort()
        for construction in batimentj2:
            construction.mort()
        print("\033[95m {}\033[00m".format(territoire))
        if territoire[0] == 2:
            victoire[1] = True
        elif territoire[9] == 1:
            victoire[0] = True


class CarteDeBatiment(Carte):
    def __init__(self, place, vie, nom, faction, description, equipe):
        super().__init__(nom, faction, description, equipe)
        self.vie = vie
        self.place = place

    def degat(self, damage):
        self.vie -= damage
        print("\033[35m {}\033[00m".format(
            str("il reste " + str(self.vie) + " point de vie à " + self.nom + " de " + self.faction)))
        self.mort()

    def utilisation(self):
        global tour
        print("Joueur ", self.equipe, " choisisser un emplacement")
        case = int(input("emplacement"))
        if case == "stop":
            tour[0] -= 1
        elif 0 <= case >= 9:
            if territoire[case] == self.equipe:
                if emplacement[case] == 0:
                    emplacement[case] = self.equipe
                    if self.equipe == 1:
                        batimentj1.append(self)
                    else:
                        batimentj2.append(self)
                    emplacement[case] = self.equipe
                    self.place = case
                else:
                    print("\033[91m {}\033[00m".format(
                        "il y a déjà un batiment ici, si vous n'avez pas d'emplacement libre écriver : stop"))
                    self.utilisation()
            else:
                print("\033[91m {}\033[00m".format("emplacement invalide vous n'avez pas ce territoire"))
                self.utilisation()
        else:
            print("\033[91m {}\033[00m".format("c'est pas une case ça c'est même pas comprise entre 0 et 9"))
            self.utilisation()

    def mort(self):
        if self.vie <= 0 or territoire[self.place] != self.equipe:
            if self.equipe == 1:
                batimentj1.remove(self)
            else:
                batimentj2.remove(self)
            emplacement[self.place] = 0
            print("\033[95m {}\033[00m".format(str(self.nom) + " de " + str(self.faction) + "c'est éfondré."))


class CarteDeBatimentAttaque(CarteDeBatiment):
    def __init__(self, attaque, attaque_recente, place, vie, nom, faction, description, equipe):
        super().__init__(place, vie, nom, faction, description, equipe)
        self.attaque = attaque
        self.attaque_recente = attaque_recente

    def attaquer(self, cible):
        cible.degat(self.attaque)


"""
class CarteDeBatimentBuff(CarteDeBatiment):
    def __init__(self, bonus, place, vie, nom, faction, description, equipe):
        super().__init__(place, vie, nom, faction, description, equipe)
        self.bonus = bonus


class CarteDeBatimentMur(CarteDeBatiment):
    def __init__(self, place, vie, nom, faction, description, equipe):
        super().__init__(place, vie, nom, faction, description, equipe)
"""


class Crystal(Carte):
    def __init__(self, place, vie, nom, faction, description, equipe):
        super().__init__(nom, faction, description, equipe)
        self.vie = vie
        self.place = place
        if self.equipe == 1:
            emplacement[0] = 1
            self.place = 0
            batimentj1.append(self)
        else:
            emplacement[9] = 2
            self.place = 9
            batimentj2.append(self)

    def degat(self, damage):
        self.vie -= damage
        print("\033[35m {}\033[00m".format(
            str("il reste " + str(self.vie) + " point de vie à " + self.nom + " de " + self.faction)))
        if self.equipe == 1:
            if self.vie <= 0:
                victoire[1] = True
        else:
            if self.vie <= 0:
                victoire[0] = True


def choixfaction(numero):
    global textes
    boucle = True
    while boucle:
        compteur = 0
        factionj = str(
            input("\033[92m {}\033[00m".format(str("Joueur " + str(numero) + " choisisser parmi: " + textes))))
        for nation in liste_faction:
            if factionj == nation:
                liste_faction.remove(nation)
                faction_choisie.append(factionj)
                boucle = False
            compteur += 1
        if compteur == len(liste_faction) and boucle:
            print("\033[91m {}\033[00m".format("nom de faction invalide"))
    textes = ""
    for r in range(len(liste_faction)):
        if r != len(liste_faction) - 1:
            textes = textes + str(liste_faction[r]) + ", "
        else:
            textes = textes + str(liste_faction[r]) + "."


def carte_plante(team):
    carte_plante1 = CarteDeTerritoire(20, "ronces", "plante", "des ronces sortes du sol et font progresser le territoire de 20 %", team)
    carte_plante11 = CarteDeTerritoire(10, "herbes", "plante", "des ronces sortes du sol et font progresser le territoire de 10 %", team)
    carte_plante111 = CarteDUnite(50, 20, False, "plante carnivore", "plante", "ouepp", team)
    carte_plante1111 = CarteDeBatimentAttaque(50, False, None, 50, "test batiment", "plante", "description", team)
    return [carte_plante1, carte_plante11, carte_plante111, carte_plante1111]


def carte_terre(team):
    carte_terre1 = CarteDeTerritoire(20, "tremblement de terre", "terre", "des ronces sortes du sol et font progresser le territoire de 20 %", team)
    carte_terre11 = CarteDeTerritoire(10, "éruption", "terre", "des ronces sortes du sol et font progresser le territoire de 10 %", team)
    carte_terre111 = CarteDUnite(50, 20, False, "golem", "terre", "ouepp", team)
    return [carte_terre1, carte_terre11, carte_terre111]


def carte_eau(team):
    carte_eau1 = CarteDeTerritoire(20, "marée haute", "eau", "invoque une marée qui fait progresser le territoire de 20 %", team)
    carte_eau11 = CarteDeTerritoire(10, "marée moins-haute", "eau", "invoque une marée qui fait progresser le territoire de 10 %", team)
    carte_eau111 = CarteDUnite(50, 20, False, "kraken", "eau", "ouepp", team)
    return [carte_eau1, carte_eau11, carte_eau111]


def carte_feu(team):
    carte_feu1 = CarteDeTerritoire(20, "montée de lave", "feu", "invoque une marée qui fait progresser le territoire de 20 %", team)
    carte_feu11 = CarteDeTerritoire(10, "vague de flamme", "feu", "invoque une marée qui fait progresser le territoire de 10 %", team)
    carte_feu111 = CarteDUnite(50, 20, False, "soldats", "feu", "ouepp", team)
    return [carte_feu1, carte_feu11, carte_feu111]


def carte_magie(team):
    carte_magie1 = CarteDeTerritoire(20, "marée haute", "magie", "invoque une marée qui fait progresser le territoire de 20 %", team)
    carte_magie11 = CarteDeTerritoire(10, "marée moins-haute", "magie", "invoque une marée qui fait progresser le territoire de 10 %", team)
    carte_magie111 = CarteDUnite(50, 20, False, "kraken", "magie", "ouepp", team)
    return [carte_magie1, carte_magie11, carte_magie111]


def carte_tenebre(team):
    carte_tenebre1 = CarteDeTerritoire(20, "marée haute", "tenebre", "invoque une marée qui fait progresser le territoire de 20 %", team)
    carte_tenebre11 = CarteDeTerritoire(10, "marée moins-haute", "tenebre", "invoque une marée qui fait progresser le territoire de 10 %", team)
    carte_tenebre111 = CarteDUnite(50, 20, False, "kraken", "tenebre", "ouepp", team)
    return [carte_tenebre1, carte_tenebre11, carte_tenebre111]


def association(un_nombre):
    if faction_choisie[un_nombre] == "plante":
        return carte_plante(un_nombre+1)
    elif faction_choisie[un_nombre] == "feu":
        return carte_feu(un_nombre+1)
    elif faction_choisie[un_nombre] == "terre":
        return carte_terre(un_nombre+1)
    elif faction_choisie[un_nombre] == "magie":
        return carte_magie(un_nombre+1)
    elif faction_choisie[un_nombre] == "tenebre":
        return carte_tenebre(un_nombre+1)
    else:
        return carte_eau(un_nombre+1)


# début du jeu
choixfaction(1)
liste_de_cartej1 = association(0)
choixfaction(2)
liste_de_cartej2 = association(1)
crystalj1 = Crystal(None, 500, "crystal_du_j1", faction_choisie[0], "objectif à détruire pour l'ennemi", 1)
crystalj2 = Crystal(None, 500, "crystal_du_j2", faction_choisie[1], "objectif à détruire pour l'ennemi", 2)
while not(victoire[0]) and not(victoire[1]):
    question = ("\033[93m {}\033[00m" .format(str("Joueur " +
                                                  str((tour[0] % 2)+1) + " Liste des commandes : Jouer une "
                                                                         "carte [Carte] (fin du tour), "
                                                                         "utiliser une unité [unite] (pas la "
                                                                         "fin du tour),\n attaquer avec un "
                                                                         "bâtiment [batiment] (pas la fin du "
                                                                         "tour).")))
    action = str(input(question))
    if tour[0] % 2 == 0:
        for i in unitej2:
            i.attaque_recente = False
        for i in batimentj2:
            try:
                i.attaque_recente = False
            except:
                pass
        if action == "Carte":
            nomC = str(input("\033[93m {}\033[00m" .format("Nom de la Carte")))
            x = 0
            for i in liste_de_cartej1:
                if i.nom == nomC:
                    i.utilisation()
                    break
                else:
                    x += 1
            if x == len(liste_de_cartej1):
                print("\033[91m {}\033[00m" .format("Ce n'est pas une carte ça"))
                tour[0] -= 1
        elif action == "unite":
            nomC = str(input("\033[93m {}\033[00m" .format("Nom de l'unite")))
            for i in unitej1:
                if nomC == i.nom:
                    qui = str(input("\033[93m {}\033[00m" .format("Nom de la cible")))
                    a_attaque = False
                    for e in unitej2:
                        if qui == e.nom:
                            if not i.attaque_recente:
                                i.attaquer(e)
                                i.attaque_recente = True
                                tour[0] -= 1
                                a_attaque = True
                                break
                            else:
                                print("\033[91m {}\033[00m" .format("vous avez deja attaquer avec cette unite ce tour"))
                                tour[0] -= 1
                                break
                    if not a_attaque:
                        for e in batimentj2:
                            if qui == e.nom:
                                if not i.attaque_recente:
                                    i.attaquer(e)
                                    i.attaque_recente = True
                                    tour[0] -= 1
                                    a_attaque = True
                                    break
                                else:
                                    print("\033[91m {}\033[00m" .format("vous avez deja attaquer avec cette unite ce tour"))
                                    tour[0] -= 1
                                    break
                    if not a_attaque and not i.attaque_recente:
                        print("\033[91m {}\033[00m" .format("cible non trouvé"))
                        tour[0] -= 1
                        break
                else:
                    print("\033[91m {}\033[00m" .format("Unité non trouvé"))
                    tour[0] -= 1
                    break
            if len(unitej1) == 0:
                print("\033[91m {}\033[00m" .format("Tu n'as pas d'unité"))
                tour[0] -= 1
        elif action == "ff":
            victoire[1] = True
        elif action == "batiment":
            nomB = str(input("\033[93m {}\033[00m" .format("Nom du batiment :")))
            for i in batimentj1:
                if i.nom == nomB:
                    if not i.attaque_recente:
                        cible = str(input("\033[93m {}\033[00m" .format("Nom de la cible :")))
                        for e in unitej2:
                            if cible == e.nom:
                                i.attaquer(e)
                                i.attaque_recente = True
                                tour[0] -= 1
                        if not i.attaque_recente:
                            for e in batimentj2:
                                if cible == e.nom:
                                    i.attaquer(e)
                                    i.attaque_recente = True
                                    tour[0] -= 1
                        if not i.attaque_recente:
                            print("\033[91m {}\033[00m" .format("cible non trouvé"))
                            tour[0] -= 1
                            break
                    else:
                        print("\033[91m {}\033[00m" .format("vous avez déjà attaquer avec ce bâtiment ce tour"))
                        tour[0] -= 1
                        break
            if len(batimentj1) == 0:
                print("\033[91m {}\033[00m" .format("vous n'avez pas de batiment"))
                tour[0] -= 1
        else:
            print("\033[91m {}\033[00m" .format("Commande non reconu"))
            tour[0] -= 1

    else:
        for i in unitej1:
            i.attaque_recente = False
        for i in batimentj1:
            try:
                i.attaque_recente = False
            except:
                pass
        if action == "Carte":
            nomC = str(input("\033[93m {}\033[00m" .format("Nom de la Carte")))
            x = 0
            for i in liste_de_cartej2:
                if i.nom == nomC:
                    i.utilisation()
                    break
                else:
                    x += 1
            if x == len(liste_de_cartej2):
                print("\033[91m {}\033[00m" .format("Ce n'est pas une carte ça"))
                tour[0] -= 1
        elif action == "unite":
            nomC = str(input("\033[93m {}\033[00m" .format("Nom de l'unite")))
            for i in unitej2:
                if nomC == i.nom:
                    qui = str(input("\033[93m {}\033[00m" .format("Nom de la cible")))
                    a_attaque = False
                    for e in unitej1:
                        if qui == e.nom:
                            if not i.attaque_recente:
                                i.attaquer(e)
                                i.attaque_recente = True
                                tour[0] -= 1
                                a_attaque = True
                                break
                            else:
                                print("\033[91m {}\033[00m" .format("vous avez deja attaquer avec cette unite ce tour"))
                                tour[0] -= 1
                                break
                    if not a_attaque:
                        for e in batimentj1:
                            if qui == e.nom:
                                if not i.attaque_recente:
                                    i.attaquer(e)
                                    i.attaque_recente = True
                                    tour[0] -= 1
                                    a_attaque = True
                                    break
                                else:
                                    print("\033[91m {}\033[00m" .format("vous avez deja attaquer avec cette unite ce tour"))
                                    tour[0] -= 1
                                    break
                    if not a_attaque and not i.attaque_recente:
                        print("\033[91m {}\033[00m" .format("cible non trouvé "))
                        tour[0] -= 1
                else:
                    print("\033[91m {}\033[00m" .format("Unité non trouvé"))
                    tour[0] -= 1
            if len(unitej2) == 0:
                print("\033[91m {}\033[00m" .format("Tu n'as pas d'unité"))
                tour[0] -= 1
        elif action == "ff":
            victoire[0] = True
        elif action == "batiment":
            nomB = str(input("\033[93m {}\033[00m" .format("Nom du batiment :")))
            for i in batimentj2:
                if i.nom == nomB:
                    if not i.attaque_recente:
                        cible = str(input("\033[93m {}\033[00m" .format("Nom de la cible :")))
                        for e in unitej1:
                            if cible == e.nom:
                                i.attaquer(e)
                                i.attaque_recente = True
                                tour[0] -= 1
                        if not i.attaque_recente:
                            for e in batimentj1:
                                if cible == e.nom:
                                    i.attaquer(e)
                                    i.attaque_recente = True
                                    tour[0] -= 1
                        if not i.attaque_recente:
                            print("\033[91m {}\033[00m".format("cible non trouvé"))
                            tour[0] -= 1
                            break
                    else:
                        print("\033[91m {}\033[00m".format("vous avez déjà attaquer avec ce bâtiment ce tour"))
                        tour[0] -= 1
                        break
            if len(batimentj1) == 0:
                print("\033[91m {}\033[00m".format("vous n'avez pas de batiment"))
                tour[0] -= 1
        else:
            print("\033[91m {}\033[00m" .format("Commande non reconu"))
            tour[0] -= 1
    tour[0] += 1

if victoire[0]:
    print("\033[96m {}\033[00m" .format("Le joueur 1 a gagné"))
else:
    print("\033[96m {}\033[00m" .format("Le joueur 2 a gagné"))
