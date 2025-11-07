from funciones.todas_funciones import *
from recursos.preguntas import *
from copy import deepcopy
from time import sleep


# Lista de 15 casilleros (elementos del 0 al 14) para el tablero del Juego de la Vida.
casilleros = [0, 1, -1, -1, 0, 1, -1, -1, 0, 1, -1, 0, 1, 0, 1]
# pedimos Nombre
nombre = pedir_nombre()

# Bienvenida preguntar si desea jugar?
mostrar_texto(f"Hola, {nombre}. ¿Deseas jugar?:")
iniciar_partida = desea_jugar()

# Logica
# Si quiere jugar
if iniciar_partida:
    #Tablero
    mostrar_tablero(casilleros, "Tablero")

    ## Datos del jugador
    preguntas = deepcopy(preguntas) # Preguntas trivia
    puntos = 15000 # Puntos
    indices_preguntas_correcta = [] # Preguntas correctas
    ubicacion = 0
    movimientos = 0
    ## Empieza el juego
    while iniciar_partida:
        sleep(2)
        movimientos += 1
        mostrar_texto_dos(f"Movimineto {movimientos}")
        mostrar_texto(f"{nombre.capitalize()}, estas la Casilla [{ubicacion}]") # Mostramos la pocision
        dado = generar_num_aleatorio(1,6) # Tiramos dado
        mostrar_texto(f"Has tirado el dado y el resultado es: {dado}") # Mostrar dado
        ubicacion += dado # Guardamos la pocision
        iniciar_partida = verificar_pocision(ubicacion, casilleros) # verificamos pocision
        ## Reconpensas
        if iniciar_partida:
            mostrar_texto(f"Has avanzado hasta la casilla: {ubicacion}\nFeliciades te salio: {casilleros[ubicacion - 1]}")
            puntos += reconpensa(casilleros, preguntas, indices_preguntas_correcta, ubicacion)
            iniciar_partida = verificar_puntos(0, puntos)
        else:
            mostrar_texto(f"Gracias por participar quedo en la ubicaion: [{ubicacion}]")
        mostrar_texto(f"Puntos totale: {puntos}")
        ## Deseas seguir jugando -------------------------------
        mostrar_texto(f"{nombre}, ¿deseas volver a tirar el dado?")
        iniciar_partida = desea_jugar()
    ## Mostramos datos alcanzados
    if ubicacion > len(casilleros):
        mostrar_texto(f"Felicidades gano llebo  la ubicacion: [{ubicacion}]")
## No quiere jugar
else:
    mostrar_texto(f"!Entendido¡, {nombre} sera para la proxima")


