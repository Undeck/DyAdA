import time
class Cosa ():
    nombre = ""
def __init__ (self, nombre, precio, peso, llevado):
    self.nombre = nombre
    self.precio = precio
    self.peso = peso
    self.llevado = llevado
    self.valor = precio/peso
def  evalua (num, arregloCosas, restriccion):
    pos = 0
    ganancia = 0
    peso = 0
    cad=bin(num)
    cad = cad[2:]
    cad = cad.rjust(len(arregloCosas))
    cad = cad.replace ("", "0")
    for l in cad:
        if l == "1":
            ganancia += arregloCosas [pos].precio
            peso += arregloCosas[pos].peso
        pos+=1
    if peso > restriccion:
        return -1       #Posibles convinaciones n^2
    else:               #
        return ganancia
    
inicio = time.time()
print("Robando con busqueda exaustiva")
arregloCosas = []
arregloCosas.append(Cosa('Cuaderno',20,2,0))
arregloCosas.append(Cosa('libro',10,1,0))
arregloCosas.append(Cosa('licuadora',100,10,0))
maximo = 0
mejorcombina = 0
for c in range (pow(2,len(arregloCosas)))
    obtenido = evalua (c,arregloCosas,20)
    if obtenido > maximo:
        mejorCombina = c
        maximo = obtenido
print(mejorCombina)
fin = time.time
tiempo = fin - inicio
print ("timepo requerido=",tiempo,"segundos")


