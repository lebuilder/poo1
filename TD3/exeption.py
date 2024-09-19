class MonException(Exception): # (1)
    def __init__(self, val1: float, val2: float):
        Exception.__init__(self)
        self.__msg:str = "ok"
        if val1 <= 0 or val2 <= 0:
            self.__msg = "les valeurs doivent être strictement positives"
    def __str__(self) -> str: # (2)
        return self.__msg
    
if __name__ == "__main__":
    """division de deux nombres compris entre 0 et 100"""
# declaration des variables
a: float = None
b: float = None
q: float = None
try:
    # saisie
    a = float(input("a strictement positif : "))
    b = float(input("b strictement positif : "))
    # controle de la saisie
    raise MonException(a, b) 

except MonException as mex: 
    print(mex)
    
except(Exception, KeyboardInterrupt) as ex:
    print("message d'erreur : ", ex)

print("fin du programme")