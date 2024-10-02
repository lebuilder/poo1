import random

class Devine(Exception):
    NB_TENTATIVES: int = 0
    NB_MAGIQUE: int = None
    FIN: bool = False

    def __init__(self, proposition: int):
        self.__proposition = proposition
        Devine.NB_TENTATIVES += 1
        if Devine.NB_TENTATIVES > 10:
            Devine.FIN = True
        elif self.__proposition == Devine.NB_MAGIQUE:
            Devine.FIN = True

    def __str__(self) -> str:
        if Devine.NB_TENTATIVES > 10:
            return "trop tard, tu es lent comme une limace"
        elif self.__proposition < Devine.NB_MAGIQUE:
            return "trop petit, il faut voir plus grand dans la vie"
        elif self.__proposition > Devine.NB_MAGIQUE:
            return "trop grand, vois pas aussi grand dans la vie"
        else:
            return f"bravo, tu as trouvé en {Devine.NB_TENTATIVES} tentatives, tu aurai pus faire mieux"

    @staticmethod
    def set_nb_magique():
        Devine.NB_MAGIQUE = random.randint(0, 100)

    @staticmethod
    def get_fin() -> bool:
        return Devine.FIN

if __name__ == "__main__":
    valeur: int = None
    Devine.set_nb_magique()
    while not Devine.get_fin():
        try:
            valeur = int(input("entre un nombre et plus vite que sa  : "))
            raise Devine(valeur)  # une exception est levée à chaque nouvelle proposition
        except Devine as mex:
            print(mex)
        except ValueError:
            print("erreur de saisie ... un nombre est attendu, tu es trop con sérieux ")