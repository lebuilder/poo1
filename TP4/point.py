import os
import time

LARGEUR = 80
HAUTEUR = 24

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
    def affiche_derniere_ligne(msg:str)->None:
        # compléter la ligne avec des espaces
        i:int = len(str(msg))+1 
        while i < LARGEUR:
            msg += " "
            i += 1
        print(f"\033[{HAUTEUR+1};1H{msg}")
        

if __name__ == "__main__":
    os.system("clear")
    Point.affiche_car(1,1,"x")
    Point.affiche_car(1,HAUTEUR,"e")
    Point.affiche_car(LARGEUR,1,'°')
    Point.affiche_car(LARGEUR,HAUTEUR,"_")
