import random
import time

n = 2350 * 10        #Numero = 1900
lista = []
while len(lista)<n:
    ale = random.randint (1,n)
    if not (ale in lista):
        lista.append(ale)
#print(lista)

inicio=time.time()

for j in range(n):
    for i in range(n-1):
        if lista[i]>lista[i+1]:
            lista[i],lista[i+1] = lista[i + 1], lista[i]
fin = time.time()        #mide el tiempo
print(fin-inicio)

