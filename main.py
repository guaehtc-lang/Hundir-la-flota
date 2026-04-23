from game.tablero import crear_tablero, mostrar_tablero, mostrar_tablero_oculto
from game.ships import crear_barcos, colocar_barcos
from game.game_logic import disparar
from services.input_output import pedir_coordenadas, disparo_ia
from game.game_logic import comprobar_fin

# Crear tablero jugador
tablero = crear_tablero()

# Crear tablero IA
tablero_ia = crear_tablero()

# Crear barcos
barcos = crear_barcos()

# Crear barcos IA
barcos_ia = crear_barcos()

# Colocar barcos en tablero jugador
tablero, barcos = colocar_barcos(tablero, barcos)
print("")
print("==============================")
print("        TABLERO JUGADOR")
print("==============================")
mostrar_tablero(tablero)

# Colocar barcos en tablero IA
tablero_ia, barcos_ia = colocar_barcos(tablero_ia, barcos_ia)
print("")
print("==============================")
print("        TABLERO IA")
print("==============================")
mostrar_tablero_oculto(tablero_ia)

# Disparo del usuario

while True:

    #fila, columna= disparo_ia()
    fila, columna = pedir_coordenadas()
    resultado_jugador = disparar(tablero_ia, fila, columna)
    print("Resultado:", resultado_jugador)
    print("")
    print("")
    print("==============================")
    print("      TABLERO JUGADOR")
    print("==============================")
    mostrar_tablero(tablero)
    print("")
    print("==============================")
    print("        TABLERO IA")
    print("==============================")
    mostrar_tablero_oculto(tablero_ia)
    print("")
    
    if comprobar_fin(barcos_ia, tablero_ia):
        print("HAS GANADO")
        break

    #if resultado == "ya_disparado":
    #    print("Ya habías disparado ahí")
    #    continue

    if resultado_jugador == "tocado":
        print("Has acertado, dispara otra vez")
        continue

# Si llega aquí → agua, cambia jugador, disparo IA
    print("Turno de la IA")
    
    fila_ia, columna_ia = disparo_ia()
    resultado_ia = disparar(tablero, fila_ia, columna_ia)
    print("Resultado IA:", resultado_ia)
    print("")
    print("")
    print("==============================")
    print("      TABLERO JUGADOR")
    print("==============================")
    mostrar_tablero(tablero)
    print("")
    print("==============================")
    print("        TABLERO IA")
    print("==============================")
    mostrar_tablero_oculto(tablero_ia)
    print("")
    
    if comprobar_fin(barcos, tablero):
        print("LA IA HA GANADO")
        break

    #if resultado == "ya_disparado":
    #    print("Ya habías disparado ahí")
    #    continue

    if resultado_ia == "tocado":
        print("repite IA")
        continue
