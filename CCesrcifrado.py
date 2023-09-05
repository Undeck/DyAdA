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

print(cifraCesar('todos', 8))