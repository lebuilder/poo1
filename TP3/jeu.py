#!/usr/bin/python
# coding:utf-8
import random
import time
import os

if __name__ == "__main__":
    MIN = 10
    MAX = 50
    tempo = 0.2
    nb_secret = random.randint(MIN, MAX)
    fin:bool = False

    print("Vous devez arrêter le programme sur", nb_secret)
    print("Pour arrêter le programme, il faut faire Ctrl+C")
    input("Appuyer sur Entrée pour commencer ...")

    i = 0
    while i < MAX and not fin:
        try:
            i += 1
            os.system("cls" if os.name == "nt" else "clear")
            print("Vous devez arrêter le programme sur", nb_secret)
            print(i)
            time.sleep(tempo)
        except KeyboardInterrupt:
            fin = True
            if i == nb_secret:
                print("\nBravo! Vous avez arrêté le programme sur le nombre secret:", nb_secret)
            else:
                print("\nVous avez arrêté le programme sur le mauvais nombre:", i)
        finally:
            print("Fin du programme")