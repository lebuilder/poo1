from abc import ABC, abstractmethod

class Courrier(ABC):
    def __init__(self, poids: float, adresse: str):
        self.poids = poids
        self.adresse = adresse

    def valide(self) -> bool:
        return bool(self.adresse)

    @abstractmethod
    def affranchir(self) -> float:
        pass # On ne peut pas instancier une classe abstraite 

    def get_poids(self) -> float:
        return self.poids

    def __str__(self) -> str:
        validite = "valide" if self.valide() else "invalide"
        return f"Courrier {validite}, Poids: {self.poids}g, Destination: {self.adresse}, Prix: {self.affranchir()}€"

class Lettre(Courrier):
    def __init__(self, poids: float, adresse: str, format: str):
        super().__init__(poids, adresse)
        self.format = format

    def affranchir(self) -> float:
        prix = 1 if self.format == "A4" else 2
        return prix + self.poids / 1000

    def __str__(self) -> str:
        return f"Lettre\n{super().__str__()}, Format: {self.format}"

class Colis(Courrier):
    def __init__(self, poids: float, adresse: str, volume: float):
        super().__init__(poids, adresse)
        self.volume = volume

    def valide(self) -> bool:
        return super().valide() and self.volume <= 50

    def affranchir(self) -> float:
        return 0.25 * self.volume + self.poids / 1000

    def __str__(self) -> str:
        return f"Colis\n{super().__str__()}, Volume: {self.volume} litres"

class Boite:
    def __init__(self):
        self.courriers = []

    def ajouter_courrier(self, courrier: Courrier):
        self.courriers.append(courrier)

    def affranchissement(self) -> float:
        return sum(courrier.affranchir() for courrier in self.courriers)

    def courriers_invalides(self) -> int:
        return sum(not courrier.valide() for courrier in self.courriers)

    def __str__(self) -> str:
        return "\n".join(str(courrier) for courrier in self.courriers)

if __name__ == "__main__":
    # Déclarer trois références d'objets de type Courrier
    lettre = Lettre(800, "", "A4")
    colis1 = Colis(5000, "IUT de Lannion", 30)
    colis2 = Colis(3000, "Place des Mouettes", 70)

    # Afficher les caractéristiques des trois courriers
    print(lettre)
    print(colis1)
    print(colis2)

    # Seconde partie
    print("-------------gestion d'une boite------------------------")
    # Déclarer une référence de boite de courriers
    boite = Boite()

    # Ajouter les 3 courriers à la boite
    boite.ajouter_courrier(lettre)
    boite.ajouter_courrier(colis1)
    boite.ajouter_courrier(colis2)

    # Ajouter un nouveau courrier
    nouvelle_lettre = Lettre(500, "Rue de la Paix", "A3")
    boite.ajouter_courrier(nouvelle_lettre)

    # Afficher les caractéristiques des courriers de la boite
    print(boite)

    # Afficher le nombre de courriers invalides de la boite
    print(f"Nombre de courriers invalides: {boite.courriers_invalides()}")