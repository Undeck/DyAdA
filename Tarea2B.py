def Cdiccionario(archivo):         #Definimos Cdiccionario para despues cargarle el txt
    diccionario = {}               #Creamos el diccionario vacio para almacenar palabras
    with open(archivo, 'r') as archivo: #abrimos el archivo txt en modo lectura
        for linea in archivo:           #Iniciamos el bucle para leer las definiciones
            palabra, definicion = linea.strip().split(': ') #dividimos en 2 Palabra y Definicion
            diccionario[palabra] = definicion   #agrefamos la palabra y el significado en la variable diccionario
    return diccionario

def buscar_definicion(diccionario, palabra):    #Definimos buscar_diccionario
    if palabra in diccionario:          #Verificamos si la palabra existe en el diccionario
        return diccionario[palabra]     #Arrojamos la palabra
    else:
        return "La palabra no fue encontrada en el diccionario."    #Si no exite nos da error

def main():        #Definimos Main para hacerla nuestra funcion principal
    txt = "words.txt"       #definimos que la variable diccionario corresponde al archivo words.txt
    diccionario = Cdiccionario(txt)

    while True:     #iniciamos un bucle infinito para que no nos saque cada que pongamos una palabra
        palabra_buscar = input("Ingrese una palabra para su definición (o 'dsalir' para salir): ") #pedimos la palabra
        if palabra_buscar.lower() == 'dsalir': #convertimos la palabra a minusculas
            break
        definicion = buscar_definicion(diccionario, palabra_buscar)
        print(definicion)

if __name__ == "__main__":
    main()
