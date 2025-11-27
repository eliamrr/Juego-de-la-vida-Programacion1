from funciones.todas_funciones import *
from recursos.preguntas import *
from copy import deepcopy
casilleros = [0, 1, -1, -1, 0, 1, -1, -1, 0, 1, -1, 0, 1, 0, 1] # Lista de 15 casilleros (elementos del 0 al 14) para el tablero del Juego de la Vida.
mostrar_texto_con_diseño("El juego de la vida")
print("a) Jugar\nb) Score \nc) Salir\n")
opcion = pedir_respuesta("a", "b", "c")
if opcion == "a":
    nombre = pedir_nombre() # pedimos Nombre
    print(f"Hola, {nombre}. ¿Deseas jugar?:") # Bienvenida preguntar si desea jugar?
    iniciar_partida = desea_jugar()
    # Logica
    if iniciar_partida: #Si quiere jugar
        mostrar_tablero(casilleros, "Tablero") #Tablero
        # Datos del jugador
        jugador = {
            "nombre": nombre,
            "preguntas" : deepcopy(preguntas), # Preguntas trivia
            "puntos" : 15000, # Puntos
            "indices_preguntas_correcta" : [], # Preguntas correctas
            "ubicacion" : 0,
            "movimientos" : 0, #estetica
            "ultimo_dado": None, #estetica
            "vida": True
        }
        while jugador["vida"]:  ## Empieza el juego
            jugador["vida"] = jugar_turno(jugador,casilleros)
            # Reconpensas
            if jugador["vida"]:
                print(f"Te salio el dado: {jugador['dado']}\nHas avanzado hasta la casilla: {jugador['ubicacion']}\nFeliciades te salio: {casilleros[jugador['ubicacion'] - 1]}")
                jugador['puntos'] += reconpensa(casilleros, preguntas, jugador['indices_preguntas_correcta'], jugador['ubicacion'])        
                print(f"Puntos actualizados: {jugador['puntos']}")
                # Deseas seguir jugando -------------------------------
                print(f"{'-'*50}\n{nombre}, ¿deseas volver a tirar el dado?")
                jugador["vida"]= desea_jugar()
            if jugador["vida"] == False:
                print(f"\n¡{jugador['nombre']}, gracias por jugar!\nPuntos finales: {jugador['puntos']}")
elif opcion == "b":
    try:
        lista_datos = leer_datos('sads.csv')
        lista_datos = crear_dic_jugador(lista_datos)
        mostrar_datos_csv(lista_datos)
    except:
        print("No hay datos para mostrar")
else: #No quiere jugar
    print(f"!Entendido¡, sera para la proxima")










