
# Hundir la Flota en Python

Proyecto del juego **Hundir la Flota** desarrollado en Python para ejecutarse en terminal.

El objetivo de este proyecto ha sido construir una versión funcional del juego, trabajando una estructura ordenada por archivos, la lógica de turnos y la organización del código de una forma clara y sencilla.

---

## Descripción

Este proyecto implementa una versión en consola del juego Hundir la Flota.

Actualmente permite:

- crear el tablero del jugador
- crear el tablero de la IA
- colocar barcos de forma aleatoria
- colocar barcos en horizontal o vertical
- evitar solapamientos
- disparar al tablero enemigo
- disparos aleatorios por parte de la IA
- marcar agua y tocado
- comprobar el final de la partida
- ocultar los barcos del tablero de la IA

---

## Estructura del proyecto

```text
battleship/
│
├── main.py
│
├── game/
│   ├── tablero.py
│   ├── ships.py
│   ├── game_logic.py
│
├── services/
│   ├── input_output.py


## Requisitos

```bash
pip install numpy
```

## Cómo ejecutar

```terminal
python main.py
```

## Autor

Juan Jesús García González



