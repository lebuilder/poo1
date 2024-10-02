import os
from threading import Thread
import random
import time
from typing import List, Tuple

LARGEUR:int = 80
HAUTEUR:int = 22

class Point:
    
    def __init__(self, x: int=0, y:int= HAUTEUR, car: str="")-> None:
        self.__x = x
        self.__y = y
        self.__car = car
    def affiche_car(self,x: int, y: int, car: str)-> None:
        # méthode générique
        # utilisation des codes d'échappement ANSI pour l'affichage dans la console
        # print("\033[y;xHchaine") Using ANSI escape sequence, moves curser to row y, col x:
        chaine: str = f"\033[{y};{x}H{car}"
        print(chaine)
    def affiche(self)-> None:
        # affiche le caractère à la position (x,y)
        self.affiche_car(self.__x, self.__y, self.__car)
        self.derniere_ligne()
    def efface(self)-> None:
        # affiche un espace à la position (x,y)
        self.affiche_car(self.__x, self.__y, " ")
        self.derniere_ligne()
    def derniere_ligne(self)-> None:
        # positionne le prompt en derniere ligne
        self.affiche_car(1,HAUTEUR,"")
    

class EtoileEphemere (Thread, Point):
    
    def __init__ (self,x:int,y:int,t_sommeil:float, t_visible:float) -> None:
        Point.__init__(self, x, y, car="*")
        Thread.__init__(self)
        self.__x = x
        self.__y = y
        self.__t_sommeil = t_sommeil
        self.__t_visible = t_visible
        
    def run(self)-> None:
        time.sleep(self.__t_sommeil)
        Point.affiche(self)
        time.sleep(self.__t_visible)
        Point.efface(self)
        
        
    
    def get_visible(self)->bool:
        return self.__t_visible


def affiche_derniere_ligne(msg:str)->None:
        # compléter la ligne avec des espaces
        i:int = len(str(msg))+1
        while i < LARGEUR:
            msg += " "
            i += 1
        print(f"\033[{HAUTEUR+1};1H{msg}")

def compte_etoiles(arg:Tuple)-> int:
    return arg


if __name__ == '__main__':
    # declaration des variables
    liste_etoiles:List[EtoileEphemere]
    nb_etoiles:int
    nb:int
    x:int # compris entre 1 et LARGEUR
    y:int # compris entre 1 et HAUTEUR
    duree:float # duree = temps maxi
    temps_sommeil:float
    tempo_visible:float
    # initialisation et instanciation
    liste_etoiles = []
    nb_etoiles = 100
    duree = 5.0
    os.system('clear')
    # boucle pour générer les etoiles et les ajouter à la liste
    nb = 0
    while nb < nb_etoiles:
        # generer aléatoirement x, y, temps_sommeil, temps_visible
        x = random.randint(1, LARGEUR)
        y = random.randint(1, HAUTEUR)
        temps_sommeil = random.uniform(0.1, duree)
        tempo_visible = random.uniform(0.1, duree)
        # ajouter une nouvelle étoile à la liste
        etoile = EtoileEphemere(x, y, temps_sommeil, tempo_visible)
        liste_etoiles.append(etoile)
        nb = nb +1
    # boucle pour lancer les threads
    for etoile in liste_etoiles:
        etoile.start()
    # compter le nombre d'étoiles toutes les 30 ms
        time.sleep(0.03)
        print(compte_etoiles(liste_etoiles))
        affiche_derniere_ligne(f"nb etoiles:{nb_etoiles}")
