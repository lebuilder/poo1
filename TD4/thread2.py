from threading import Thread, current_thread
from random import random
import time

class Classe_compteur1:
    def __init__(self, nom: str, nb_maxi: int):
        self.__nom:str = nom
        self.__nb_maxi:int = nb_maxi
    def compte(self)-> None:
        compteur:int = 0
        pause:float
        while compteur <self.__nb_maxi:
            pause = 0.5 + 0.5 * random() # pause aléatoire entre 0.5 et 1 seconde
            print(f"{self.__nom}: {compteur} pause: {pause:.2f} s")
            time.sleep(pause)
            compteur += 1
        print(self.__nom + " a terminé de compter")
        
if __name__ == "__main__":
    cpt1:Classe_compteur1
    cpt2:Classe_compteur1
    Th1: Thread
    Th2: Thread
    
    #instantiation
    cpt1 = Classe_compteur1("Cpt1",10)
    cpt2 = Classe_compteur1("Cpt2",5)
    
    Th1 = Thread(target=cpt1.compte)
    Th2 = Thread(target=cpt2.compte)
    
    # lancement 
    Th1.start()
    Th2.start()
    
    