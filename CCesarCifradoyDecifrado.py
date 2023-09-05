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
a = 'tnwfhl vasl s whvhl'
b = cifraCesar(a,8)
print (b)
print (decifraCesar(b,8))

'''for llave in range(26):
   print(decifraCesar(a,llave),llave)'''      #Sirve para ver las posibles combinaciones