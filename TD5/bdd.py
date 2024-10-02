import sqlite3
if __name__ == "__main__":
    # déclaration des variables
    nom_bdd:str
    connecteur:sqlite3.Connection
    curseur:sqlite3.Cursor
    requete: str
    reponse:tuple # pour réponse unique
    reponses:list[tuple] # pour réponses mutiples
    nom_bdd = "TD5/cine2.sqlite3"
    # connecteur à la BDD 
    connecteur = sqlite3.connect(nom_bdd)
    # création d'un curseur (pour exécuter les requètes)
    curseur = connecteur.cursor()
    # ecriture de la requète
    requete = """SELECT t_producteurs.nom, t_producteurs.prenom
                    FROM t_producteurs
                    WHERE t_producteurs.id = 1;"""
    print(requete)
    # exécution de la requète
    curseur.execute(requete)
    # lecture du résultat unique
    reponse = curseur.fetchone()
    print(reponse)