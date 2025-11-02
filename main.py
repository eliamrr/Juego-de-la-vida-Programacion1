from funciones.todas_funciones import *
from recursos.preguntas import *
from copy import deepcopy

# Lista de 15 casilleros (elementos del 0 al 14) para el tablero del Juego de la Vida.
casilleros = [0, 1, -1, -1, 0, 1, -1, -1, 0, 1, -1, 0, 1, 0, 1]
historial = []

# pedimos Nombre
nombre = pedir_nombre()
puntos = 15000
preguntas = deepcopy(preguntas)

#preguntar si desea jugar
iniciar_a_jugar = desea_jugar(nombre)

#Logica
if iniciar_a_jugar:
    inicio = True
    while inicio:
        ## Tiramos dado
        numero_randon_dado = tirar_dado(1,6)
        ## Guardamos la pocision
        guardar_pocision(historial, numero_randon_dado)
        ## Verificamos la pocision
        inicio = verificar_pocision(casilleros, historial)
        ## Condicionales
        if inicio:
            ## Extracion de reconpensa
            puntos += reconpensa(casilleros, preguntas, numero_randon_dado)
            ## Verifica puntos 
            inicio = verificar_puntos(0, puntos)
