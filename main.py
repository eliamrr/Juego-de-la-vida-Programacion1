from funciones.todas_funciones import *
from recursos.preguntas import *
from copy import deepcopy
from time import sleep

casilleros = [0, 1, -1, -1, 0, 1, -1, -1, 0, 1, -1, 0, 1, 0, 1] # Lista de 15 casilleros (elementos del 0 al 14) para el tablero del Juego de la Vida.
nombre = pedir_nombre() # pedimos Nombre
mostrar_texto(f"Hola, {nombre}. ¿Deseas jugar?:") # Bienvenida preguntar si desea jugar?
iniciar_partida = desea_jugar()
# Logica
if iniciar_partida: #Si quiere jugar
    mostrar_tablero(casilleros, "Tablero") #Tablero
    ## Datos del jugador
    jugador = {
        "nombre": nombre,
        "preguntas" : deepcopy(preguntas), # Preguntas trivia
        "puntos" : 15000, # Puntos
        "indices_preguntas_correcta" : [], # Preguntas correctas
        "ubicacion" : 0,
        "movimientos" : 0,
        "ultimo_dado":None,
        "vida":True
    }
    while jugador["vida"]:  ## Empieza el juego
        sleep(2)
        jugador["vida"] = jugar_turno(jugador,casilleros)
        ## Reconpensas
        if jugador["vida"]:
            mostrar_texto(f"Te salio el dado: {jugador["dado"]}\nHas avanzado hasta la casilla: {jugador["ubicacion"]}\nFeliciades te salio: {casilleros[jugador["ubicacion"] - 1]}")
            jugador["puntos"] += reconpensa(casilleros, preguntas, jugador["indices_preguntas_correcta"], jugador["ubicacion"])        
            mostrar_texto(f"Puntos actualizados: {jugador['puntos']}")
            ## Deseas seguir jugando -------------------------------
            mostrar_texto(f"{"-"*50}\n{nombre}, ¿deseas volver a tirar el dado?")
            jugador["vida"]= desea_jugar()
        if jugador["vida"] == False:
            mostrar_texto(f"\n¡{jugador['nombre']}, gracias por jugar!\nUbicaion final: {jugador["ubicacion"]}\nPuntos finales: {jugador['puntos']}")
else: #No quiere jugar
    mostrar_texto(f"!Entendido¡, {nombre} sera para la proxima")


