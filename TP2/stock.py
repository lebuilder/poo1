class Article:
    #1. Les modificateurs :   
        #•Un constructeur qui permettra de modifier tous les attributs, il fera appel à la méthode set() ci dessous.
        #•Le modificateur set() qui permettra de modifier tous les attributs avec une seule méthode.
        #•La méthode acheter() qui permet d’acheter un certain nombre d’articles (le nombre sera un paramètre de la méthode), la méthode retourne le prix à payer.
    # 2. Les observateurs :   
        # •get() qui retourne l’ensemble des attributs de l’objet sous la forme d’une chaîne de caractères.
        # •get_nom() qui retourne le nom de l’article
        # •get_quantite() qui retourne la quantité de l’article.
        # •get_attributs() qui retourne un tuple avec tous les attributs
        # •get_dict() qui retourne un dictionnaire avec l’ensemble des attributs (clé = nom de l’attribut, valeur = valeur de l’attribut)
    def __init__(self) -> None:
        self.__nom: str
        self.__quantite: int = 0
        self.__prixunit: float = 0.0

    def set(self , nom: str, quantite: int, prixuint: float)-> None:
        self.__nom = nom
        self.__quantite = quantite
        self.__prixunit = prixuint
        

    def acheter(self, nb_acheter)-> None:
        return self.__prixunit * nb_acheter

    def get(self)-> None:
        return f"Nom: {self.__nom}, Quantité: {self.__quantite}, Prix unitaire: {self.__prixunit}"

    def get_nom(self)-> str:
        return self.__nom

    def get_quantite(self)-> int:
        return self.__quantite

    def get_attributs(self)-> tuple:
        return (self.__nom, self.__quantite, self.__prixunit)

    def get_dict(self)-> None:
        return {"Nom": self.__nom, "Quantité": self.__quantite, "Prix unitaire": self.__prixunit}

if __name__ == "__main__":
    print ("------- premiere partie, des objects simples-------")
    # declaration de 3 references d objets nommés a1, a2 et a3
    a1: Article
    a2: Article
    a3: Article
    # instanciation des 3 objets
    a1 = Article()
    a2 = Article()
    a3 = Article()
    # 100 bols a 10.23€, 50 chemises a 45.32€ et 35 guitares a 150)
    a1.set("bol", 100, 10.23)
    a2.set("chemise", 50, 45.32)
    a3.set("guitare", 35, 150)
    # affichage des attributs des articles avec la methode get()
    print(a1.get())
    print(a2.get())
    print(a3.get())
    # afficher le dictionnaire de chaque objet avec l'attribut __dict__ puis avec votre méthode 
    print(a1.__dict__)
    print(a2.__dict__)
    print(a3.__dict__)
    
    print(a1.get_dict())
    print(a2.get_dict())
    print(a3.get_dict())
    # acheter 5 elements au 1er article et afficher de cout correspondant
    print(a1.acheter(5))
    
    
    # acheter 3 elements de 2eme article et afficher de cout correspondant
    print(a2.acheter(3))
    
    # afficher a nouveau les attributs des articles avec la methode get_attributs()
    print(a1.get_attributs())
    print(a2.get_attributs())
    print(a3.get_attributs())