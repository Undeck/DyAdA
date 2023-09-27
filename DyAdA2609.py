def cifraSustitucion(cad, llave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    miAlfabeto = 'cfhjlmgxbatzusyonpvdeqriwk'
    cad = cad.lower()   # Convierte el texto a minúsculas
    cifrado = ''
    for c in cad:
        if c in alfabeto:
            pos = alfabeto.index(c)
            cifrado = cifrado + miAlfabeto[pos]  
        else:
            cifrado += c 
    return cifrado

miAlfabeto = 'cfhjlmgxbatzusyonpvdeqriwk' 
texto = 'hola'
print(cifraSustitucion(texto, miAlfabeto))

a="este es un texto de prueba un poco mas grande" \
"para poder ejercitar algunas estructuras de datos" \
"tales como el diccionario y tambien hacer un" \
"ataque por analisis de frecuencias"

b = cifraSustitucion(a, miAlfabeto)
print(b)
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
frecuencias = {}
for c in alfabeto:
    frecuencias [c] = 0
print(frecuencias)
for e in a:     #a += 1    equivale a     a = a + 1
    if e in alfabeto:
        frecuencias[e]+= 1
print(frecuencias)
