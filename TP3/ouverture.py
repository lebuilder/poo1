while True:
    filename = input("Entrez le nom du fichier à lire : ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
            break
    except IOError:
        print("Le fichier n'existe pas. Veuillez essayer un autre nom de fichier.")