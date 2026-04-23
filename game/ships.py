import random

def crear_barcos():
    barcos = [
        {"tamano": 4, "posiciones": []},
        {"tamano": 3, "posiciones": []},
        {"tamano": 3, "posiciones": []},
        {"tamano": 2, "posiciones": []},
        {"tamano": 2, "posiciones": []},
        {"tamano": 2, "posiciones": []}
    ]
    return barcos


def colocar_barco(tablero, barco):
    colocado = False

    while not colocado:

        orientacion = random.choice(["H", "V"])

        if orientacion == "H":
            fila = random.randint(0, 9)
            columna = random.randint(0, 10 - barco["tamano"])
        else:
            fila = random.randint(0, 10 - barco["tamano"])
            columna = random.randint(0, 9)

        posiciones = []
        puede_colocar = True

        for i in range(barco["tamano"]):
            if orientacion == "H":
                if tablero[fila][columna + i] != " ":
                    puede_colocar = False
            else:
                if tablero[fila + i][columna] != " ":
                    puede_colocar = False

        if puede_colocar:
            for i in range(barco["tamano"]):
                if orientacion == "H":
                    tablero[fila][columna + i] = "B"
                    posiciones.append((fila, columna + i))
                else:
                    tablero[fila + i][columna] = "B"
                    posiciones.append((fila + i, columna))

            barco["posiciones"] = posiciones
            colocado = True

    return tablero, barco

def colocar_barcos(tablero, barcos):
    for barco in barcos:
        tablero, barco = colocar_barco(tablero, barco)
    return tablero, barcos


# Prueba
# from tablero import crear_tablero, mostrar_tablero
# tablero = crear_tablero()
# barcos = crear_barcos()
# tablero, barcos = colocar_barcos(tablero, barcos)
# mostrar_tablero(tablero)
# print(barcos)