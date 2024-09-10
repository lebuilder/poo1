class Complexe:
    # declaration de la variable statique
    MODE_REPRESENTATION: str = "math" # ou "elec"
    def __init__(self):
        # declaration des attributs
        self.__reel: float = 0.0
        self.__img: float = 0.0
    def set_rectangulaire(self,reel: float, img: float)->None:
        self.__reel = reel
        self.__img = img
    def set_polaire(self,ro: float, teta: float)->None:
        pass
    def get_reel(self)-> float :
        return self.__reel
    def get_img(self)-> float :
        return self.__img
    def get(self)-> str:
        chaine:str = "erreur"
        if Complexe.MODE_REPRESENTATION == "math":
            chaine= f"{self.get_reel} + i.{self.get_img}"
        elif Complexe.MODE_REPRESENTATION == "elec":
            chaine= f"{self.get_reel} + jjjjjj.{self.get_img}"
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

    # instanciez z1, z2, z3
    
    # initialisez z1 avec les valeurs [1.0 ; 45.0°]
    
    # instanciez z2 avec les valeurs Re= 0.7071 Im=-0.7071
    
    # afficher les 3 complexes
    
    print("---------suite------------")
    # Modifier les coordonnées de z3 avec les valeurs : Ro=2.0 Téta=90.0
    ...
    # copier z3 dans z4 en utilisant la méthode copy du module copy
    ...
    # modification de z3 pour vérification avec les valeurs Re=0.0 et Im=0.0
    ...
    # afficher z4
    ...
    # Multiplier z1 par z2 et mettre le résultat dans z5
    ...
    # Ajouter z1 par z2 et mettre le résultat dans z6
    ...
    print("---------nouveau mode affichage------------")
    # changer le mode d'affichage et afficher les – complexes