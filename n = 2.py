n = 17
delta = 2
raiz = 0
error = 0.00001
while abs (raiz * raiz -n) > error:
    raiz = raiz + delta
    if raiz * raiz > n:
        raiz = raiz - delta
        delta = delta/10
    print (raiz)
print(raiz)