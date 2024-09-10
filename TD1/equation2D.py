class Personne:
    def __init__(self, nom:str, age:int):
        self.__nom: str = nom
        self.__age: int = age
    def get_nom(self)->str:
        return self.__nom

    def __str__(self) -> str: # surdefinition de la méthode __str__()
        return f"{self.__nom} age : {str(self.__age)} ans"
    
if __name__ == "__main__":

    #Déclaration des références d'objets
    p1: Personne
    p2: Personne
    dict_p1 = {"nom" : "titi", "age": 14}
    dict_p2 = {"nom" : "bob", "age": 15}
    #Instances des objets
    p1 = Personne("toto",21)
    p2 = Personne("tata",22)

    #Affichage des attributs
    print(p1.get_nom())
    print(p2.get_nom())
    #pour avoir la joli phrase
    print(p1.__str__())

    #Affichage des dictionnaire des objets
    print(p1.__dict__)
    print(p2.__dict__)
