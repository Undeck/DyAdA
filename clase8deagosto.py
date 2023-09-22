b = "hola buenos dias a todos en este jueves de septiembre"
print(len(b))
print(b.split())#separa la oracion
c = b.split() 
print(len(c))
print(b[2])
print(c[2])
c.sort() 
print (c) #imprime las palabras ordenadas'''

'''a = "esto es una cadena de prueba para un ejercicio en clase"\
"y queremos crear un pequeÃ±o diccionario para una tarea"\
"donde vamos a quitar palabras repetidas"
b = a.split()
c =[]
for Pal in b:
    if not (Pal in c):
        c.append(Pal)
c.sort()
print(c, len(c))'''    

d = [1,2,3,4,5,7,11]
e = [1,2,5,7,9]
f = [1,2,1,3,1,2,3,1]
print(f)
'''g = set(f)
print(g)'''
f = list(set(f))
print(f)
