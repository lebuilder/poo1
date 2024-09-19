class Bureau:
    def __init__(self, num_bureau: int):
        self.__num_bureau = num_bureau

    def get(self) -> str:
        return f" numéro de bureau : {self.__num_bureau}"

class Employe:
    # constructeur
    def __init__(self, nom: str):
        # attributs
        self.__nom: str = nom

    # observateur
    def get(self) -> str:
        return self.__nom

class Secretaire(Employe): # la classe mère entre parenthèse (1)
    # constructeur
    def __init__(self, nom: str, num_bureau: int):
        Employe.__init__(self, nom) # appel au constructeur classe mère (2)
        self.__bureau = Bureau(num_bureau)
        
    # observateur
    def get(self) -> str: # surdéfinition de la méthode get() (4)
        chaine: str = Employe.get(self) + self.__bureau.get()
        return chaine

if __name__ == "__main__":
    # declaration d'une reference de type Secretaire
    secretaire = Secretaire("Anne", 105)
    # affichage de la chaîne retournée par la méthode get()
    print(secretaire.get())