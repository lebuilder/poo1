from threading import Timer

def fonction_timer(msg: str, tempo: int, nb_appels: int) -> None:
    if nb_appels > 0:
        print(msg)
        nb_appels -= 1
        Timer(tempo, fonction_timer, args=(msg, tempo, nb_appels)).start()

# Pour démarrer la fonction évoluée
fonction_timer("Message affiché toutes les 2 secondes", 2, 5)