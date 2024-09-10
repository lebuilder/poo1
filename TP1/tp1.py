import math
import copy
class Complexe:
    # declaration de la variable statique
    MODE_REPRESENTATION: str = "math" # ou "elec"

    def __init__(self):
        # declaration des attributs
        self.__reel: float = 0.0
        self.__img: float = 0.0

    def set_rectangulaire(self,reel: float, img: float)->None:
        # Fonction qui permet de définir en mode rectangulaire
        self.__reel = reel
        self.__img = img

    def set_polaire(self,ro: float, teta: float)->None:
        # Fonction qui permet de définir en mode polaire
        self.__reel = ro * math.cos(teta*math.pi/180)
        self.__img = ro * math.sin(teta*math.pi/180)

    def get_reel(self)-> float :
        # Fonction qui permet de récupéré le reel 
        return self.__reel
    
    def get_img(self)-> float :
        # Fonction qui permet de récupéré le nombre imaginaire
        return self.__img
    
    def get_ro(self)->float:
        # Fonction qui permet de récupéré le ro 
        return math.sqrt(self.__reel*self.__reel + self.__img*self.__img)
    
    def get_teta(self)-> float:
        # Fonction qui permet de récupéré le tata
        return 180/math.pi * math.atan(self.__img/self.__reel)

    def get(self)-> str:
        chaine:str = "erreur"
        if Complexe.MODE_REPRESENTATION == "math":
            chaine= f"{self.__reel} + i.{self.__img}"
        elif Complexe.MODE_REPRESENTATION == "elec":
            chaine= f"[ {self.get_ro()} ; {self.get_teta()} ]"
        return chaine
    
    @staticmethod
    def set_mode_affichage(mode: str)->None:
        if mode in ("math", "elec"):
            Complexe.MODE_REPRESENTATION = mode # modification de la variable statique



            
if __name__== "__main__":

    #Afficher le mode de représentation
    print(Complexe.MODE_REPRESENTATION)

    # déclarez variables de type Complexe nommés z1, z2, z3, z4 et z5
    z1:Complexe
    z2:Complexe
    z3:Complexe
    z4:Complexe
    z5:Complexe
    z6:Complexe

    # instanciez z1, z2, z3
    z1 = Complexe()
    z2 = Complexe()
    z3 = Complexe()
    z4 = Complexe()
    z5 = Complexe()
    z6 = Complexe()
    
    # initialisez z1 avec les valeurs [1.0 ; 45.0°]
    z1.set_polaire(1, 45)
    
    # instanciez z2 avec les valeurs Re= 0.7071 Im=-0.7071
    z2.set_rectangulaire(0.7071 , -0.7071)
    
    # afficher les 3 complexes
    print(z1.get())
    print(z2.get())
    # print(z3.get()) pas de valeur pour z3 
    
    print("---------suite------------")
    # Modifier les coordonnées de z3 avec les valeurs : Ro=2.0 Téta=90.0
    z3.set_polaire(2.0 , 90.0)
    # copier z3 dans z4 en utilisant la méthode copy du module copy
    z4  =copy.copy(z3)
    # modification de z3 pour vérification avec les valeurs Re=0.0 et Im=0.0
    z3.set_rectangulaire(0.0 , 0.0)
    # afficher z4
    print(z4.get())
    # Multiplier z1 par z2 et mettre le résultat dans z5

    z5.set_rectangulaire(z1.get_reel() * z2.get_reel() - z1.get_img() * z2.get_img(), z1.get_reel() * z2.get_reel() + z1.get_img() * z2.get_img())
    print(z5.get())
    # Ajouter z1 par z2 et mettre le résultat dans z6

    z6.set_rectangulaire(z1.get_reel() + z2.get_reel(), z1.get_img() + z2.get_img() )
    print(z6.get())
    print("---------nouveau mode affichage------------")
    # changer le mode d'affichage et afficher les – complexes
    Complexe.set_mode_affichage("elec")
    print(z1.get())
    print(z2.get())
    print(z4.get())
    print(z5.get())
    print(z6.get())