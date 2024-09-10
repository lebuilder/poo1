class Ville:
    #get_attributs() qui retournera les attributs sous la forme d’un tuple.
    # get() qui retournera une chaîné de caractères décrivant tous les attributs d'une ville.
    # get_dict() qui retournera les attributs sous la forme d’un dictionnaire.
    # get_nom() qui retourne le nom de la ville
    # get_nb_habitants() qui retourne le nombre d’habitants de la ville

    def __init__(self, nom: str, nb_habitants: int) -> None:
        self.__nom: str = nom
        self.__nb_habitants: int = nb_habitants
        
    def get_attributs(self) -> tuple:
        return (self.__nom, self.__nb_habitants)
    
    def get(self) -> str:
        return f"Nom: {self.__nom}, Nombre d'habitants: {self.__nb_habitants}"
    
    def get_dict(self) -> dict:
        return {"Nom": self.__nom, "Nombre d'habitants": self.__nb_habitants}
    
    def get_nom(self) -> str:
        return self.__nom
    
    def get_nb_habitants(self) -> int:
        return self.__nb_habitants    
    
    
    # get_attributs() qui retournera les attributs sous la forme d’un tuple.
    # get() qui retournera une chaîné de caractères décrivant tous les attributs d'une capitale.
    # get_dict() qui retournera les attributs sous la forme d’un dictionnaire.
    # get_pays() qui retourne le nom du pays
class Capitale(Ville):
    def __init__(self, nom: str, nb_habitants: int, pays: str) -> None:
        Ville.__init__(self, nom, nb_habitants)
        self.__pays: str = pays
    
    def get_attibuts(self)-> tuple:
        return (self.get_nom(), self.get_nb_habitants(), self.__pays)
    
    def get(self) -> str:
        return f"Nom: {self.get_nom()}, Nombre d'habitants: {self.get_nb_habitants()}, Pays: {self.__pays}"
    
    def get_dict(self)-> dict:
        return {"Nom": self.get_nom(), "Nombre d'habitants": self.get_nb_habitants(), "Pays": self.__pays}
    
    def get_pays(self)-> str:
        return self.__pays

if __name__ == "__main__":
    print("----------objets simples-----------")
    # déclarer les références de 2 villes et 1 capitale
    ville1 = Ville("Rospez", 1681)
    ville2 = Ville("Perros_Guirec", 7440)
    capital1= Capitale("Lannion", 19920, "Tregor")
    
    
    # instancier les 3 objets
    # ROSPEZ, 1681 habitants
    # PERROS_GUIREC, 7440 habitants
    # LANNION 19920, habitants, capitale du TREGOR
    ...
    # afficher tous les attributs des villes et des capitales
    ville1_attributs = ville1.get_attributs()
    ville2_attributs = ville2.get_attributs()
    capital1_attributs = capital1.get_attibuts()
    # afficher les noms des villes et capitales
    nom_ville1 = ville1.get_nom()
    nom_ville2 = ville2.get_nom()
    nom_capital1 = capital1.get_nom()
    print("----------liste de villes et capitale------------")
    # déclarer la référence d'un liste de Ville appelée liste_Villes
    liste_villes = list()
    # instanciez la liste des villes
    
    # ajouter les 3 villes déclarées individuellement à la liste des villes
    liste_villes.append(ville1)
    liste_villes.append(ville2)
    liste_villes.append(capital1)
    # ajouter une ville à la liste
    # RENNES 220 488 habitants, capitale de la BRETAGNE
    liste_villes.append(Capitale("Rennes", 220488, "Bretagne"))
    
    print("----------affichez attributs des villes et capitales : ")
    for ville in liste_villes:
        print(ville.get())
        
    print("----------affichez les noms des villes et capitales : ")
    for ville in liste_villes:
        print(ville.get_nom())
    print("----------affichez les attributs des villes uniquement: ")
    for ville in liste_villes:
        if isinstance(ville, Ville):
            print(ville.get())
    print("----------affichez population complète-----------")
    pop_total = sum(ville.get_nb_habitants() for ville in liste_villes)
    print(f"Population totale: {pop_total}")