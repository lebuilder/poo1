
class Employe:
    def __init__(self, dictionnaire: dict) -> None:
        self.__nom = dictionnaire.get("_Employe__nom", "")
        self.__age = dictionnaire.get("_Employe__age", 0)
        self.__pays = dictionnaire.get("_Employe__pays", "")
        self.__anniversaire = dictionnaire.get("_Employe__anniversaire", "")
        self.__id = dictionnaire.get("_Employe__id", 0)
        self.__internet = dictionnaire.get("_Employe__internet", False)
        self.__langue = dictionnaire.get("_Employe__langue", "")
        self.__genre = dictionnaire.get("_Employe__genre", "")

    def get_nom(self) -> str:
        return self.__nom

    def get_age(self) -> int:
        return self.__age

    def get_id(self) -> int:
        return self.__id

    def get_pays(self) -> str:
        return self.__pays

    def get_anniversaire(self) -> str:
        return self.__anniversaire

    def get_internet(self) -> bool:
        return self.__internet

    def get_langue(self) -> str:
        return self.__langue

    def get_genre(self) -> str:
        return self.__genre

if __name__ == "__main__":
    dict_p = {
        "_Employe__nom": "etienne",
        "_Employe__age": 34,
        "_Employe__pays": "france",
        "_Employe__anniversaire": "1988-12-27",
        "_Employe__id": 227417393,
        "_Employe__internet": False,
        "_Employe__langue": "francais",
        "_Employe__genre": "homme"
    }
    
    # déclarez une variable de type Employe
    employe = Employe(dict_p)
    
    # affichez les attributs en utilisant les observateurs
    print(f"Nom: {employe.get_nom()}")
    print(f"Age: {employe.get_age()}")
    print(f"Pays: {employe.get_pays()}")
    print(f"Anniversaire: {employe.get_anniversaire()}")
    print(f"ID: {employe.get_id()}")
    print(f"Internet: {employe.get_internet()}")
    print(f"Langue: {employe.get_langue()}")
    print(f"Genre: {employe.get_genre()}")