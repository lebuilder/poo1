import numpy as np
import matplotlib.pyplot as plt
import math

def courbe(x):
    try:
        if x == 0:
            return 1  
        else:
            return math.sin(x) / x
    except Exception as e:
        print(f"Erreur lors du calcul de sin({x})/{x}: {e}")
        return None

def main():
    try:
        # Generate x values from -20 to 20 with a step of 0.5
        x_values = np.arange(-20, 20, 0.5)
        
        # Calculate y values
        y_values = [courbe(x) for x in x_values]
        
        # Plot the curve
        plt.plot(x_values, y_values, label='sin(x)/x')
        plt.title('Courbe de sin(x)/x')
        plt.xlabel('x')
        plt.ylabel('sin(x)/x')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    except Exception as e:
        print(f"Erreur lors de l'exécution du programme: {e}")
    finally:
        print("Fin du programme")

if __name__ == "__main__":
    main()