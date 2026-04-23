import random

def pedir_coordenadas():
    x = int(input("Introduce fila (0-9): "))
    y = int(input("Introduce columna (0-9): "))
    return x, y

def disparo_ia():
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    return x, y
