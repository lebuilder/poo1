import os 

HAUTEUR:int = 22
LARGEUR:int = 80


def affiche_car(x:int, y:int, car:str)-> None:
    # méthode générique
    # utilisation des codes d'échappement ANSI pour l'affichage dans la console
    # print("\033[y;xHchaine") Using ANSI escape sequence, moves curser to row y, col x:
    chaine:str = f"\033[{y};{x}H{car}"
    print(chaine)
    

if __name__ == "__main__":
    os.system("clear")
    affiche_car(1,1,"x")
    affiche_car(1,HAUTEUR,"e")
    affiche_car(LARGEUR,1,'°')
    affiche_car(LARGEUR,HAUTEUR,"_")