from random import randint

def pedir_nombre()->str:
    "Funcion que pìde el nombre del jugador y lo retorna"
    nombre = input("Nombre: ")
    while len(nombre) <= 0:
        nombre = input("Por favor ingrese un nombre: ")
    return nombre

def mostrar_texto(texto:str):
    "Funcion que recibe un texto y lo muestra por pantalla"
    print(texto)

def desea_jugar()-> bool:
    retornar = False
    print(f"> Si\n> No ")
    respuesta = input("Ingrese: (Si/No): > ").lower()
    while respuesta != "si" and respuesta != "no":
        respuesta = input("Error, ingrese (Si/No): > ").lower()
    if respuesta == "si":
        retornar = True
    return retornar

def generar_num_aleatorio(desde:int, hasta:int)-> int:
    numero_randon = randint(desde,hasta)
    return numero_randon


def verificar_pocision(ubicaion:int, casilleros:list) -> bool:
    retorno = False
    if ubicaion <= len(casilleros):
        retorno = True
    return retorno

def reconpensa(casilleros:list,preguntas:list, list_ind_preg_correctas:list, dado:int)-> int:
    casillero = casilleros[dado]
    puntos_nuevos = 0
    if casillero == 1:
        puntos_nuevos += 3000
    elif casillero == -1:
        puntos_nuevos -= 3000
    else:
        ind_preg_aleatoria = generar_num_aleatorio(0, len(preguntas) - 1) # genera un indice de pregunta aleatoria
        mostrar_pregunta(preguntas, ind_preg_aleatoria)
        respuesta = pedir_respuesta("a", "b", "c") # Respueta
        comprobar_respuesta = verificar_respuesta(preguntas, ind_preg_aleatoria, respuesta )
        if comprobar_respuesta:
            puntos_nuevos += 3000
            list_ind_preg_correctas.append(ind_preg_aleatoria)
        else:
            puntos_nuevos -= 3000
        # Eliminamos preguntas
        eliminar_pregunta(preguntas, ind_preg_aleatoria)
    mostrar_texto(f"Has obtenido {puntos_nuevos} puntos")
    return puntos_nuevos


def mostrar_pregunta(lista:list, indice:int):
    print(f"{"-"*20}Pregunta{   "-"*20}")
    print(f"{lista[indice]["pregunta"]}")
    print(f"a) {lista[indice]["respuesta_a"]}")
    print(f"b) {lista[indice]["respuesta_b"]}")
    print(f"c) {lista[indice]["respuesta_c"]}")
    
def pedir_respuesta(a:str,b:str,c:str)->str:
    respuesta = input(f"Responda con {a} {b} {c}: ").lower()
    while respuesta != a and respuesta != b and respuesta != c:
        respuesta = input(f"Error, responda con {a} {b} {c}: ").lower()
    return respuesta
    
def verificar_respuesta(lista:list, indice:int ,respuesta:str)->bool:
    retornar = False
    if lista[indice]["respuesta_correcta"] == respuesta:
        retornar = True
    return retornar
        
def eliminar_pregunta(lista:list, indice:int)->int:
    del lista[indice]

def verificar_puntos(minimo:int, puntos:int):
    seguir = True 
    if puntos <= minimo:
        mostrar_texto("Se quedo sin puntos, juego terminado")
        seguir = False
    return seguir



