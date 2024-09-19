class Personne:
    def __init__(self, nom: str):
        self.__nom = nom
    def get(self)-> str:
        return self.__class__.__name__ + " : " + self.__nom
    
class Etudiant(Personne):
    
    def __init__(self, nom: str, formation: str):
        Personne.__init__(self, nom)
        self.__formation = formation
    def get(self)-> str:
        return f"{Personne.get(self)} formation : {self.__formation}"
    
class Alternant(Etudiant):
    def __init__(self, nom: str, formation: str, entreprise: str):
        Etudiant.__init__(self, nom, formation)
        self.__entreprise = entreprise
    def get(self)-> str:
        return f"{Etudiant.get(self)} entreprise : {self.__entreprise}"
    
class Ancien(Etudiant):
    def __init__(self, nom: str, formation: str, annee_diplome: str):
        Etudiant.__init__(self, nom, formation)
        self.__annee_diplome = annee_diplome
    def get(self)-> str:
        return f"{Etudiant.get(self)} dilopme en : {self.__annee_diplome}"
if __name__ == "__main__":
    liste_pers: list[Personne] 
    liste_pers = list()
    liste_pers.append(Ancien("papy", "R&T", 2002))
    liste_pers.append(Alternant("Kim", "MMI", "Orange"))
    liste_pers.append(Etudiant("Toto", "R&T"))
    
    # afficher les caractéristique de chaque étudiant
    for pers in liste_pers:
        print(pers.get())
        print()