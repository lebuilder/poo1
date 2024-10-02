from threading import Thread, Lock
from random import random
import time

class CompteurThread(Thread):
    def __init__(self, nom: str, nb_maxi: int):
        Verrou :Lock = Lock()
        Thread.__init__(self, name=nom)
        self.__nb_maxi:int = nb_maxi
    def run(self)-> None:
        compteur:int = 0
        pause:float
        with CompteurThread.Verrou :
            while compteur <self.__nb_maxi:
                pause = 0.5 + 0.5 * random() # pause aléatoire entre 0.5 et 1 seconde
                print(f"{self.getName()}: {compteur} pause: {pause:.2f} s")
                time.sleep(pause)
                compteur += 1
        print(self.getName() + " a terminé de compter")
        
if __name__ == "__main__":
    
    cpt1:CompteurThread
    cpt2:CompteurThread
    cpt1 = CompteurThread("Cpt1",10)
    cpt2 = CompteurThread("Cpt2",5)
    
    cpt1.start()
    cpt2.start()