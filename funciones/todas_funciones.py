def pedir_nombre()->str:
    "Funcion que pìde el nombre del jugador y lo retorna"
    nombre = input("Nombre: ")
    return nombre

def desea_jugar(name:str)-> bool:
    retornar = False
    print(f"{name} deseas jugar?\n> Si\n> No ")
    respuesta = input("Ingrese (Si/No): > ").lower()
    while respuesta != "si" and respuesta != "no":
        respuesta = input("Error, ingrese (Si/No): > ").lower()
    if respuesta == "si":
        retornar = True
    return retornar
    
def tirar_dado(desde:int, hasta:int)-> int:
    from random import randint
    numero_randon = randint(desde,hasta)
    return numero_randon

def guardar_pocision(lista:list, pocision:int):
    lista.append(pocision)

def suma_lista(lista:list):
    suma_total = 0
    for i in lista:
        suma_lista += i
    return suma_total

def verificar_pocision(lista_a_recorrer,lista_pocision:list):
    seguir = True
    pocision = suma_lista(lista_pocision)
    pocision -=1
    if pocision > len(lista_a_recorrer):
        descripcion_juego("Juego terminado")
        seguir = False
    return seguir

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
    if lista[indice]["respuesta:_correcta"] == respuesta:
        retornar = True
    return retornar
def eliminar_pregunta(lista:list, indice:int)->int:
    del lista[indice]

def reconpensa(casilleros:list, preguntas:list,dado:int):
    respuesta = casilleros[dado]
    if respuesta == 1:
        puntos  += 3000
    elif respuesta == -1:
        puntos -= 3000
    else:
        pregunta_randon = tirar_dado(0,len(preguntas - 1))
        mostrar_pregunta(preguntas,pregunta_randon)
        respuesta = pedir_respuesta("a","b","c")
        respuesta_final = verificar_respuesta(casilleros, pregunta_randon, respuesta)
        if respuesta_final:
            puntos += 3000
            eliminar_pregunta(casilleros, pregunta_randon)
        else:
            puntos -= 3000
    return puntos

def descripcion_juego(texto:str):
    print(texto)

def verificar_puntos(minimo:int, puntos:int):
    seguir = True 
    if puntos <= minimo:
        descripcion_juego("Se quedo sin puntos, juego terminado")
        seguir = False
    return seguir



