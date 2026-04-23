import numpy as np

def crear_tablero():
    tablero = np.full((10,10)," ")
    #tablero = np.full((5,5),"B")
    #Elemina # para probar y poneselo a la linea de la misma variable
    
    return tablero

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        
def mostrar_tablero_oculto(tablero):
    for fila in tablero:
        # guardamos la fila que voy a enseñar
        fila_visible = []

        for casilla in fila:
            if casilla == "B":
                fila_visible.append(" ")
            else:
                fila_visible.append(casilla)
        
        print(" | ".join(fila_visible))

# Prueba
#tablero = crear_tablero()
#mostrar_tablero(tablero)
#mostrar_tablero_oculto(tablero)