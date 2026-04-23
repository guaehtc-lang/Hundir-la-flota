def disparar(tablero, fila, columna):

    if tablero[fila][columna] == "B":
        tablero[fila][columna] = "X"
        return "tocado"
    
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = "O"
        return "agua"

    return "ya_disparado"

def comprobar_fin(barcos, tablero):

    for barco in barcos:

        for (fila, columna) in barco.posiciones:
            if tablero[fila][columna] != "X":
                return False

    # si todas estan tocadas, se acaba la partida
    return True