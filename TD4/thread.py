from threading import Thread, current_thread
from random import random
import time

class Compteur:
    def fonction_compteur(self,nb_maxi: int)->None:
        nom:str = current_thread().name # (1)
        compteur:int = 0
        pause:float
        while compteur < nb_maxi:
            pause = 0.5 + 0.5 * random() # pause aléatoire entre 0.5 et 1 seconde
            print(f"{nom}: {compteur} pause: {pause:.2f} s")
            time.sleep(pause)
            compteur += 1
        print(nom + " a terminé de compter")
        
if __name__ == "__main__":
    
    # Variables
    th1 :Thread # premier tread
    th2 :Thread # second thread
    
    Cpt1 = Compteur
    Cpt2 = Compteur
    
    #Instantiation 
    Cpt1 = Compteur()
    Cpt2 = Compteur()
    th1 = Thread(target=Cpt1.fonction_compteur , name="Cpt1", args=(5,) ) # l'argument doit être un tuple 
    th2 = Thread(target=Cpt2.fonction_compteur , name="Cpt2", args=(4,) )
    
    # Démarrage
    th1.start()
    th2.start()
    
    