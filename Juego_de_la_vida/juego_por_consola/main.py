from funciones.todas_funciones import *
from recursos.preguntas import *
from copy import deepcopy
casilleros = [0, 1, -1, -1, 0, 1, -1, -1, 0, 1, -1, 0, 1, 0, 1] # Lista de 15 casilleros (elementos del 0 al 14) para el tablero del Juego de la Vida.
mostrar_texto_con_diseño("El juego de la vida")
print("a) Jugar\nb) Score \nc) Salir\n")
opcion = pedir_respuesta("a", "b", "c")
if opcion == "a":
    jugador = {
        "nombre": None,
        "preguntas" : deepcopy(preguntas), # Preguntas trivia
        "puntos" : 15000, # Puntos
        "indices_preguntas_correcta" : [], # Preguntas correctas
        "ubicacion" : 0,
        "movimientos" : 0, #estetica
        "vida": None
    }
    jugador["nombre"] = pedir_nombre() # pedimos Nombre
    mostrar_tablero(casilleros, "Tablero") #Tablero
    print(f"\nHola, {jugador['nombre']} bienvenido!. ¿Deseas tirar el primer dado?:") # Bienvenida preguntar si desea jugar?
    jugador["vida"] = desea_jugar()
    while jugador["vida"]:  ## Empieza el juego
        jugador["vida"] = jugar_turno(jugador,casilleros)
        # Reconpensas
        if jugador["vida"]:
            jugador['puntos'] += reconpensa(casilleros, preguntas, jugador['indices_preguntas_correcta'], jugador['ubicacion'])        
            print(f"Puntos actualizados: {jugador['puntos']}")
            # Deseas seguir jugando -------------------------------
            print(f"{'-'*50}\n{jugador['nombre']}, ¿deseas volver a tirar el dado?")
            jugador["vida"]= desea_jugar()
    print(f"\n¡{jugador['nombre']}, gracias por jugar!\nPuntos finales: {jugador['puntos']}")          
elif opcion == "b":
    try:
        lista_datos = leer_datos('score.csv')
        lista_datos = crear_dic_jugador(lista_datos)
        mostrar_datos_csv(lista_datos)
    except:
        print("No hay datos para mostrar")
else: #No quiere jugar
    print(f"!Entendido¡, sera para la proxima")








