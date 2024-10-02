from threading import Thread
import time
import random
from typing import List, Tuple
import os

# Constantes pour les dimensions du terminal
LARGEUR = 80
HAUTEUR = 15

class Point:
    def __init__(self, x: int, y: int, car: str = '*'):
        self.__x = x
        self.__y = y
        self.__car = car

    def affiche_car(self, x: int, y: int, car: str) -> None:
        # Déplace le curseur à (x, y) et affiche le caractère
        chaine: str = f"\033[{y};{x}H{car}"
        print(chaine, end='')

    def affiche(self) -> None:
        # Affiche le caractère aux coordonnées du point
        self.affiche_car(self.__x, self.__y, self.__car)
        self.derniere_ligne()

    def efface(self) -> None:
        # Efface le caractère aux coordonnées du point
        self.affiche_car(self.__x, self.__y, " ")
        self.derniere_ligne()

    def derniere_ligne(self) -> None:
        # Positionne le curseur à la dernière ligne
        self.affiche_car(1, HAUTEUR, "")

    @staticmethod
    def affiche_derniere_ligne(msg: str) -> None:
        # Affiche un message sur la dernière ligne, en complétant avec des espaces
        i: int = len(str(msg)) + 1
        while i < LARGEUR:
            msg += " "
            i += 1
        print(f"\033[{HAUTEUR + 1};1H{msg}")

class EtoileEphemere(Thread, Point):
    def __init__(self, x: int, y: int, t_sommeil: float, t_visible: float):
        Thread.__init__(self)
        Point.__init__(self, x, y)
        self.__t_sommeil = t_sommeil
        self.__t_visible = t_visible
        self.__visible = False

    def run(self) -> None:
        # Attend pendant le temps de sommeil avant d'apparaître
        time.sleep(self.__t_sommeil)
        self.__visible = True
        self.affiche()
        # Reste visible pendant le temps de visibilité
        time.sleep(self.__t_visible)
        self.efface()
        self.__visible = False

    def get_visible(self) -> bool:
        # Retourne le statut de visibilité de l'étoile
        return self.__visible

if __name__ == '__main__':
    def compte_etoiles(arg: Tuple[EtoileEphemere, ...]) -> int:
        # Compte le nombre d'étoiles visibles
        return sum(etoile.get_visible() for etoile in arg)

    liste_etoiles: List[EtoileEphemere] = []
    nb_etoiles = 100
    duree = 5.0
    os.system("clear")  # Efface l'écran du terminal

    # Génère des étoiles et les ajoute à la liste
    for _ in range(nb_etoiles):
        x = random.randint(1, LARGEUR)
        y = random.randint(1, HAUTEUR)
        temps_sommeil = random.uniform(0, duree)
        tempo_visible = random.uniform(0.1, 1.0)
        etoile = EtoileEphemere(x, y, temps_sommeil, tempo_visible)
        liste_etoiles.append(etoile)

    # Démarre les threads pour chaque étoile
    for etoile in liste_etoiles:
        etoile.start()

    # Compte et affiche continuellement le nombre d'étoiles visibles toutes les 30 ms
    while any(etoile.is_alive() for etoile in liste_etoiles):
        nb_visibles = compte_etoiles(tuple(liste_etoiles))
        Point.affiche_derniere_ligne(f"nb etoiles visibles: {nb_visibles}")
        time.sleep(0.03)
        
