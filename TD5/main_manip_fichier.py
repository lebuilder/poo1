SEPARATEUR: str = ";"
if __name__ == "__main__":
    nom_fichier: str = "TD5/animaux.txt"
    with open(nom_fichier, mode="r+", encoding="utf-8") as fichier:
        ligne:str
        for ligne in fichier:
            ligne = ligne.replace("\n", "")
            list_str = ligne.split(SEPARATEUR)
            print(list_str)
        fichier.write(f"poulet{SEPARATEUR}noir{SEPARATEUR}6\n")