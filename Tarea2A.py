'''def cargaPalabras () :
    archivo = open ('words.txt', 'r')
    renglon = archivo.readline ()
    palabras = renglon.split ()
    print (len(palabras), 'palabras leidas') 
    return palabras

def cargaCifrado ():
    archivo = open ('textoCifrado.txt', 'r')
    renglon = archivo.readline ()
    return renglon
def cifraCesar (cadena, llave):
    if llave < 0:
        llave = 26 - llave
    cadena = cadena.lower()
    nuevaCadena = ""
    alfabeto = 'abcdefghijklmnopqrstuvxyz'
    for 1 in cadena:
        if 1 in alfabeto:
            posicionLetra = alfabeto.find(1)
            nuevaCadena = nuevaCadena + alfabeto [((posicionLetra+llave) % 26)]
        else:
            nuevaCadena = nuevaCadena + 1
        return nuevaCadena

def descifraCesar (cadena, llave):
    return cifraCesar(cadena, 26-llave)
def getAciertos(listaPalabras, diccionario):
    numAciertos = 0
    for pal in listaPalabras:
        if pal in diccionario:
            numAciertos = numAciertos + 1
    return numAciertos

palabras = cargaPalabras()
cadena = cargaCifrado()
maxAciertos = 0
posibleLlave = 0

for cont in range(26):'''

'''def cargaPalabras():
    archivo = open('words.txt', 'r')
    renglon = archivo.readline()
    palabras = renglon.split()
    print (len(palabras), 'palabras leídas')
    return palabras

def cargaCifrado():
    archivo = open('textoCifrado.txt', 'r')
    renglon = archivo.readline()
    return renglon

def cifraCesar(cadena, llave):
    if llave < 0:
        llave = 26 - llave
    cadena = cadena.lower()
    nuevaCadena = ""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'  # Corrección en el alfabeto
    for letra in cadena:  # Cambio de "1" a "letra" como variable de iteración
        if letra in alfabeto:
            posicionLetra = alfabeto.find(letra)
            nuevaCadena = nuevaCadena + alfabeto[(posicionLetra + llave) % 26]
        else:
            nuevaCadena = nuevaCadena + letra
    return nuevaCadena

def descifraCesar(cadena, llave):
    return cifraCesar(cadena, 26 - llave)

def getAciertos(listaPalabras, diccionario):
    numAciertos = 0
    for pal in listaPalabras:
        if pal in diccionario:
            numAciertos = numAciertos + 1
    return numAciertos

palabras = cargaPalabras()
cadena = cargaCifrado()
maxAciertos = 0
posibleLlave = 0

for cont in range(26):'''

    #i have learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. - maya angelou.  i attribute my success to this: i never gave or took any excuse. florence nightingale.  the best time to plant a tree was 20 years ago. the second best time is now. chinese proverb. i am not a product of my circumstances. i am a product of my decisions. stephen covey. change your thoughts and you change your world. norman vincent peale



def cargaPalabras () :    #Definimos la funcion "CargaPalabras"
    archivo = open ('words.txt', 'r')    #Damos la orden de leer el archivo "words.txt"
    renglon = archivo.readline ()        #Leemos un renglon del txt
    palabras = renglon.split ()          #Dividimos el renglon 
    print (len(palabras), 'palabras leidas')   #nos dice cuantas palabras fueron leidas 
    return palabras                        #Nos devuelve la lista de Palabras

def cargaCifrado ():        #Definimos Funcion CaraCifrado
    archivo = open ('textoCifrado.txt', 'r')    #Damos la orden de leer el archivo "textoCifrado.txt"    
    renglon = archivo.readline ()       #lee la primer linea del txt y le asigna una variable (cadena)
    return renglon          #Nos regresa la cadena

def cifraCesar (cadena, llave):     #Definimos la funcion "cifraCesar" que tiene como argumentos cadena y lalve
    if llave < 0:       #Si llave es negativa entonces llave se combierte en positivo en funcion a una cadena de 26 caracteres
        llave = 26 - llave
    cadena = cadena.lower()         #Toda la cadena a minusculas
    nuevaCadena = ""        #Cadena vacia llamada nuevCadena
    alfabeto = 'abcdefghijklmnopqrstuvwvxyz'  #definimos una cadena que tiene el alfabeto
    for 1 in cadena:        #iniciamos el bucle for que usaremos para cifrar 
        if 1 in alfabeto:
            posicionLetra = alfabeto.find(1)        #recorremos la cadena para cifrar
            nuevaCadena = nuevaCadena + alfabeto [((posicionLetra+llave) % 26)]
                #calculamos la nuea palabra cifrada y la agregamos a Nueva cadena la cual antes estaba vacia
        else:           
            nuevaCadena = nuevaCadena + 1       #si hay una letra o caracter que no este definida la deja igual
        return nuevaCadena  

def descifraCesar (cadena, llave):  #Definimos la funcion "descifraCesar" que tiene como argumentos cadena y llave
    return cifraCesar(cadena, 26-llave) #El proceso de decifrar
def getAciertos(listaPalabras, diccionario): #cuenta cuantas palabras de listaPalabras se encuentran en diccionario
    numAciertos = 0
    for pal in listaPalabras:
        if pal in diccionario:
            numAciertos = numAciertos + 1
    return numAciertos

palabras = cargaPalabras() #Carga una lista de palabras
cadena = cargaCifrado() #Carfa el mensaje cifrado para ser decifrado
maxAciertos = 0
posibleLlave = 0        #Nos dice cual es la llave mas cercana para el descifrado

for cont in range(26):  #Aplicara las 26 llaves hasta que nos de una solucion 

    #El mensaje ya decifrado es:
    #i have learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. 
    # - maya angelou.  
    # i attribute my success to this: i never gave or took any excuse. 
    # - florence nightingale.  
    # the best time to plant a tree was 20 years ago. the second best time is now. 
    # - chinese proverb. 
    # i am not a product of my circumstances. i am a product of my decisions. 
    # - stephen covey.
    # change your thoughts and you change your world. 
    # - norman vincent peale
