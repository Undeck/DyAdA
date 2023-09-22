#archivo = open('prueba.txt','w')  

'''Modos:
'w' = abre para escritura modo texto, crea o sobreescribe
'wb' lo mismo pero en binario
'r' abre para lectura
'rb' abre para lectura en binario
'a' abre para añadir
'''

'''archivo.write('linea 1')
archivo.write('linea 2')
archivo.write('linea 3')
archivo.write('palabra 1 \n \n palabra 2 \n')
archivo.close()'''

'''archivo = open('prueba.txt' , 'r')
for renglon in archivo:
    print(renglon)
archivo.close()'''

palabras = []
archivo = open('prueba.txt' , 'r', encoding='utf-8')
for renglon in archivo:
    datos = renglon.split()
    for d in datos:
        if not (d in palabras):
            palabras.append(d)
archivo.close()
print(palabras)
palabras.sort()
print (palabras)