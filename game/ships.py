import random

class Barco:
    tipo = "barco"

    def __init__(self, tamano):
        self.tamano = tamano
        self.posiciones = []
        self.hundido = False

def crear_barcos():
    barcos = [
        Barco(4),
        Barco(3),
        Barco(3),
        Barco(2),
        Barco(2),
        Barco(2)
    ]
    return barcos

def colocar_barco(tablero, barco):
    colocado = False

    while not colocado:
        # horizontal o vertical aleatorio
        orientacion = random.choice(["H", "V"])

        if orientacion == "H":
            fila = random.randint(0, 9)
            columna = random.randint(0, 10 - barco.tamano)
        else:
            fila = random.randint(0, 10 - barco.tamano)
            columna = random.randint(0, 9)

        # guardo las posiciones del barco
        posiciones = []

        puede_colocar = True

        # compruebo si no pisa otro
        for i in range(barco.tamano):
            if orientacion == "H":
                if tablero[fila][columna + i] != " ":
                    puede_colocar = False
            else:
                if tablero[fila + i][columna] != " ":
                    puede_colocar = False

        # si se puede colocar, lo pongo en el tablero
        if puede_colocar:
            for i in range(barco.tamano):
                if orientacion == "H":
                    tablero[fila][columna + i] = "B"
                    posiciones.append((fila, columna + i))
                else:
                    tablero[fila + i][columna] = "B"
                    posiciones.append((fila + i, columna))

            # guardo las posiciones
            barco.posiciones = posiciones

            # ya esta colocado
            colocado = True

    return tablero, barco


def colocar_barcos(tablero, barcos):
    for barco in barcos:
        tablero, barco = colocar_barco(tablero, barco)
    
    return tablero, barcos

#Prueba
#import numpy as np
#tablero = np.full((10,10), " ")
#barcos = crear_barcos()
#tablero, barcos = colocar_barcos(tablero, barcos)
#print(tablero)
#print(barcos[0].tamano)
#print(barcos[0].posiciones)
#print(barcos[0].hundido)