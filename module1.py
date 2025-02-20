# Créé par emili, le 28/06/2021 en Python 3.7
from termcolor import *
color = ["red", "magenta", "green", "blue", "cyan", "white", "yellow"]
mot = "bonjour"
for e in range(10):
    for i in range(7):
        cprint(mot[i], color[i], end="")
    print("")
