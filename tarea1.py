import random
import time

n = 2350 * 10
lista = []
lista1 = []
lista2 = []
while len(lista) < n:
    ale = random.randint(1, n)
    if ale not in lista:
        lista.append(ale)

for valor in lista:
    if valor < (n // 2):
        lista1.append(valor)
    else:
        lista2.append(valor)

inicio = time.time()

for j in range(len(lista1)):
    for i in range(len(lista1) - 1):
        if lista1[i] > lista1[i + 1]:
            lista1[i], lista1[i + 1] = lista1[i + 1], lista1[i]

for j in range(len(lista2)):
    for i in range(len(lista2) - 1):
        if lista2[i] > lista2[i + 1]:
            lista2[i], lista2[i + 1] = lista2[i + 1], lista2[i]

fin = time.time()

print(fin - inicio)