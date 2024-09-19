class SaisieInvalideException(Exception):
    tentatives = 0

    def __init__(self, tentative):
        super().__init__(f"Tentative {tentative}: Saisie invalide. Veuillez entrer un nombre entre 0 et 20.")
        SaisieInvalideException.tentatives += 1

    @classmethod
    def get_tentatives(cls):
        return cls.tentatives

def demander_nombre():
    while True:
        try:
            nombre = input("Veuillez saisir un nombre entre 0 et 20: ")
            if not nombre.isdigit():
                raise ValueError("Ce n'est pas un nombre.")
            nombre = int(nombre)
            if nombre < 0 or nombre > 20:
                raise SaisieInvalideException(SaisieInvalideException.get_tentatives() + 1)
            return nombre
        except ValueError as ve:
            print(f"Erreur de valeur: {ve}")
            raise SaisieInvalideException(SaisieInvalideException.get_tentatives() + 1)
        except SaisieInvalideException as sie:
            print(sie)

if __name__ == "__main__":
    try:
        nombre = demander_nombre()
        print(f"Nombre valide saisi: {nombre}")
    finally:
        print(f"Nombre de tentatives: {SaisieInvalideException.get_tentatives()}")