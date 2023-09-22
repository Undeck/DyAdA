#Nuestro Programa
def es_palin(cad):
    cad = cad.replace (" ", " ").lower()

    return cad == cad [::-1]
cadena = input ("Palindromo:")
if es_palin(cadena):
    print ("Si es")
else:
    print("No es")

