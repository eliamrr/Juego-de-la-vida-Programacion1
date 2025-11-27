from random import randint
def pedir_nombre()->str:
    "Funcion que pìde el nombre del jugador y valida que no este vacio y lo retorna."
    nombre = input("Nombre: ")
    while len(nombre) <= 0:
        nombre = input("Por favor ingrese un nombre: ")
    return nombre

def desea_jugar()-> bool:
    "Funcion que preguinta al usuario 'SI' O 'NO' Y dependiendo de eso retorna un valor booleano"
    retornar = False
    print(f"> Si\n> No ")
    respuesta = input("Ingrese: (Si/No): > ")
    respuesta = convertir_minusculas(respuesta)
    while respuesta != "si" and respuesta != "no":
        respuesta = input("Error, ingrese (Si/No): > ")
        respuesta = convertir_minusculas(respuesta)
    if respuesta == "si":
        retornar = True
    return retornar

def convertir_minusculas(palabra:str)-> str:
    "Funcion que recibe una string por parametro y lo convierte en minuscula y despues lo retorna."
    nueva_palbra = ""
    for letra in palabra:
        valor_acscci = ord(letra) #obtine el valor ascci
        if valor_acscci >= 65 and valor_acscci <= 90:
            letra = chr(valor_acscci + 32)
        nueva_palbra += letra
    return nueva_palbra


def mostrar_texto_con_diseño(texto:str):
    "Funcion que recibe un texto y lo muestra por pantalla con un diseño."
    print(f"\n{'-' * 20}{texto}{'-'*20}\n")


def generar_num_aleatorio(desde:int, hasta:int)-> int:
    "Funcion que recibe dos parametros que van a hacer de rango para generar un numero aleatorio y despues lo retorna."
    numero_randon = randint(desde,hasta)
    return numero_randon

def mostrar_pregunta(lista:list, indice:int):
    "FUncion que recibe una lista de dicionarios y un numero y va a mostar la informacion que conincidan con el indice en la lista"
    print(f"{lista[indice]['pregunta']}")
    print(f"> a) {lista[indice]['respuesta_a']}")
    print(f"> b) {lista[indice]['respuesta_b']}")
    print(f"> c) {lista[indice]['respuesta_c']}")
    
def pedir_respuesta(a:str,b:str,c:str)->str:
    "Funcion que un string por consola al usuario y valida que sea uno de los valores recibidos opor parametros"
    respuesta = input(f"Responda con ({a}, {b}, {c}): > ")
    respuesta = convertir_minusculas(respuesta)
    while respuesta != a and respuesta != b and respuesta != c:
        respuesta = input(f"Error, responda con ({a}, {b}, {c}): > ")
        respuesta = convertir_minusculas(respuesta)
    return respuesta
    
def verificar_respuesta(lista:list, indice:int ,respuesta:str)->bool:
    retornar = False
    texto = "> ¡INCORRECTO!"
    if lista[indice]["respuesta_correcta"] == respuesta:
        retornar = True
        texto = "> ¡CORRECTO!"
    print(f"{'-'*5}{texto}")
    respuesta_correcta_id = lista[indice]['respuesta_correcta']
    respuesta_correcta_texto = lista[indice][f'respuesta_{respuesta_correcta_id}']
    print(f"Respuesta correcta: {respuesta_correcta_id}) {respuesta_correcta_texto}")
    return retornar

def eliminar_pregunta(lista:list, indice:int)->int:
    "Funcion que recibe dos parametros la primera es una lista y el segundo es un indice despues la elimina el el elmento que concida con el indice en la lista "
    del lista[indice]


def mostrar_tablero(lista:list, titulo:str):
    "Funcion que recibe una lista y un string y lo muestra con un diseño"
    mostrar_texto_con_diseño(titulo)
    print(lista)

def jugar_turno(datos:dict,casilleros:list):
    iniciar_partida = datos["vida"]
    datos["movimientos"] += 1
    mostrar_texto_con_diseño(f"Movimineto {datos['movimientos']}")
    print(f"{datos['nombre']}, estas la Casilla [{datos['ubicacion']}]") # Mostramos la pocision
    dado = generar_num_aleatorio(1,6) # Tiramos dadoa
    datos["ubicacion"] += dado # Guardamos la pocision
    datos["dado"] = dado
    pocision = verificar_pocision(datos["ubicacion"], casilleros) # verificamos pocision
    puntos = verificar_puntos(0, datos["puntos"])
    if pocision and puntos:
        print(f"!Total puntos: {datos['puntos']}")
    else:
        iniciar_partida = False
        if puntos:
            print(f"Te salio el dado: {datos['dado']}")
            print(f"{datos['nombre']}, ¡GANASTE!")
            # Agregar archivo csv------------------------------------------------------
            trabajar_archivo(datos)    
        elif pocision:
            print(f"Se quedo sin puntos: {datos['puntos']}")
    return iniciar_partida


def verificar_pocision(ubicaion:int, casilleros:list) -> bool:
    "Funcion que recibe dos parametros un numero y una lista y va a devolver un bool, el cual dependera si el numero esta dentro o fuera de la cantidad de elementos del casilleros"
    retorno = False
    if ubicaion <= len(casilleros) - 1 :
        retorno = True
    return retorno

def verificar_puntos(minimo:int, puntos:int):
    "Funcion que recibe dos parametros un numero minimo y el numero que quiero corroborar que no sea menor que el minimo y dependiendo de eso va a retornar unb bool."
    seguir = True 
    if puntos <= minimo:
        print("Se quedo sin puntos, juego terminado")
        seguir = False
    return seguir

def reconpensa(casilleros:list, preguntas:list, list_ind_preg_correctas:list, ubicaion:int)-> int:
    casillero = casilleros[ubicaion - 1] 
    puntos_nuevos = 0
    if casillero == 1:
        puntos_nuevos += 3000
    elif casillero == -1:
        puntos_nuevos -= 3000
    else:
        puntos_nuevos += trivia(preguntas, list_ind_preg_correctas)
    print(f"Has obtenido: {puntos_nuevos} puntos")
    return puntos_nuevos

def trivia(preguntas:list, list_ind_preg_correctas:list)->int:
    print(f"{'-' * 20}¡Trivia!{'-'*20}")
    puntos_nuevos = 0
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
    return puntos_nuevos

# Archivo csv--------------------------------------------------------------------
def trabajar_archivo(datos:dict):
    "Funcion que recibe un dicionario y trabaja con los distintos metodos de archivos depenediendo si existe o no existe un archivo existente"
    jugador = [datos["nombre"], datos["puntos"]]
    try:
        lista_datos = leer_datos()
        agregar_dato(lista_datos, jugador)
        ordenar_lista(lista_datos)
        sobreescribir_archivo(lista_datos, "w")
    except:
        crear_archivo(jugador, "w")

def leer_datos()->list:
    "Funcion que extrae los datos de un archivo csv existente y los limpia y los guiarda en una nueva lista y los retorna en una lista"
    lista_jugadores = []
    with open("score.csv","r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            linea = convertir_minusculas(linea.rstrip())
            if linea != "nombre, puntos":
                lista_jugadores.append([linea])
    return lista_jugadores

def agregar_dato(historial:list, jugador:list):

    dato_a_agregar = convertir_minusculas(f"{jugador[0]}, {jugador[1]}")
    historial.append([dato_a_agregar])

def ordenar_lista(lista:list):
    "Funcion que recibe una lista de listas por parametro y la va a ordenar de manera ascendente por el nombre"
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i][0] > lista[j][0]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def sobreescribir_archivo(lista_datos,modo):
    "Funcion que recibe una lista modificada para agregarla a un archivo csv ya existente"
    with open("score.csv", modo) as archivo:
        texto_a_agregar = f"Nombre, Puntos \n"
        archivo.write(texto_a_agregar)
        for linea in lista_datos:
            linea = f"{linea[0]}\n"
            archivo.writelines(linea)

def crear_archivo(lista:list, modo):
    "Funcion que recibe una lista y crea un nuevo archivo y escribe los datos de la lista pasada por parametros"
    with open("score.csv", modo) as archivo:
        #Emcabezado
        texto_a_agregar = f"Nombre, Puntos \n"
        archivo.write(texto_a_agregar)
        #Escibimos datos
        texto_a_agregar = f"{lista[0]}, {lista[1]}\n"
        archivo.write(texto_a_agregar)




    











    
        










        











