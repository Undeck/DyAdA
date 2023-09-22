'''def factorial recursivo(valor):
    print ("trabajando con", valor)
    if valor == 0:
        return 1
    else:
        return valor*factorial_recursivo (valor-1) 
print (factorial_recursivo (5)) '''

def factorial_iter (n):
    print ("trabajando con", n)
    resultado = 1
    for c in range (1, n+1):
        resultado = resultado * c
    return resultado
print (factorial_iter (5))

