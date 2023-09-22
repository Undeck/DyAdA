#Cifrado cesar 
'''def cifraCesar (cad, key):
    cifrado = ""
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    cad = cad.lower() 
    for c in cad:
        if c in alfabeto:
         pos = alfabeto.index(c)
         cifrado = cifrado + alfabeto [(pos + key)%27]
        else:
           cifrado += c
    return cifrado

print(cifraCesar('hola mundo', 50))'''

#Cifrado cesar 
def cifraCesar (cad, key):
    cifrado = ""
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    cad = cad.lower() 
    for c in cad:
        if c in alfabeto:
         pos = alfabeto.index(c)
         cifrado = cifrado + alfabeto [(pos + key)%len(alfabeto)]
        else:
           cifrado += c
    return cifrado
    
#Decifrado cesar 
def decifraCesar (cad, key):
    decifrado = ""
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    cad = cad.lower() 
    for c in cad:
        if c in alfabeto:
         pos = alfabeto.index(c)
         decifrado = decifrado + alfabeto [(pos - key)%len(alfabeto)]
        else:
           decifrado += c
    return decifrado
a = 'km hmxayae fpyra smxndp'
b = cifraCesar(a,8)
print (b)
print (decifraCesar(b,8))
#para encontra la llave de la plabra
def getAciertos(prueba, dic):
    aciertos = 0
    prueba = prueba.split()
    for e in prueba:
      if e in dic:
          aciertos += 1
    return aciertos 
dic = ["abajo", "arriba", "centro", "hambre"]
maxAciertos = 0
mejorkey = 0
for key  in range (27):
   #print(decifraCesar(a, key), key)
    prueba = decifraCesar(a,key)

    aciertos = getAciertos(prueba, dic)
    if aciertos > maxAciertos:
       maxAciertos = aciertos
       mejorkey = key
print("La mejor llave es", key)
print("El texto buscado es: ")
print(decifraCesar(a,mejorkey))