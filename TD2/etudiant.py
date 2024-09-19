from typing import List, Dict
from abc import ABC, abstractmethod

class Etudiant(ABC):
    MAX_CREDITS: int = 60

    def __init__(self, nom: str):
        self.__nom = nom
        self.__liste_UE = []

    def ajouter_note(self, note: float) -> None:
        self.__liste_UE.append(note)

    def ajouter_notes(self, notes: List[float]) -> None:
        self.__liste_UE.extend(notes)

    @abstractmethod
    def calcul_credit(self) -> int:
        pass

    def get_liste_UE(self) -> List[float]:
        return self.__liste_UE

    def get_moyenne(self) -> float:
        if not self.__liste_UE:
            return 0.0
        return sum(self.__liste_UE) / len(self.__liste_UE)

    def get(self) -> str:
        return f"{self.__nom} (Etudiant) notes UE : {' '.join(map(str, self.__liste_UE))} moyenne : {self.get_moyenne():.2f} ECTS : {self.calcul_credit()}"

    def get_dict(self) -> Dict:
        return {
            "nom": self.__nom,
            "liste_UE": self.__liste_UE,
            "moyenne": self.get_moyenne(),
            "ECTS": self.calcul_credit()
        }

class EtudiantBUT(Etudiant):
    def __init__(self, nom: str):
        super().__init__(nom)

    def calcul_credit(self) -> int:
        return Etudiant.MAX_CREDITS if self.get_moyenne() >= 10 else 0

class EtudiantLP(Etudiant):
    def __init__(self, nom: str):
        super().__init__(nom)

    def calcul_credit(self) -> int:
        ue_above_10 = [note for note in self.get_liste_UE() if note > 10]
        return int((len(ue_above_10) / len(self.get_liste_UE())) * Etudiant.MAX_CREDITS) if self.get_liste_UE() else 0

if __name__ == "__main__":
    # Déclarer une variable de type liste d'étudiants appelée liste_etudiants
    liste_etudiants = []

    # Instancier le liste 
    # Ajouter 3 étudiants à la liste
    # BOB, étudiant en BUT, "BILL" étudiant en LP et CHUCK étudiant en LP
    bob = EtudiantBUT("BOB")
    bill = EtudiantLP("BILL")
    chuck = EtudiantLP("CHUCK")
    liste_etudiants.extend([bob, bill, chuck])

    # afficher les étudiants
    for etudiant in liste_etudiants:
        print(etudiant.get())

    # Ajouter 3 notes d’UE à BOB : 10, 15 et 9
    bob.ajouter_notes([10, 15, 9])

    # Ajouter 3 notes d’UE à BILL : 12, 15, 18
    bill.ajouter_notes([12, 15, 18])

    # Ajouter 3 notes d’UE également à CHUCK : 7, 12 et 15 
    chuck.ajouter_notes([7, 12, 15])

    # afficher les résultats de tous les étudiants en utilisant la méthode get()
    for etudiant in liste_etudiants:
        print(etudiant.get())

    # afficher le dictionnaire associé à chaque étudiant
    for etudiant in liste_etudiants:
        print(etudiant.get_dict())