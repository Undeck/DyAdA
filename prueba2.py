def cargaPalabras(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            print(len(palabras), 'palabras leídas')
            return palabras
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return []

nombre_archivo = 'words2.txt'
dic = cargaPalabras(nombre_archivo)
c = 0

for p in dic:
    if len(p) == 8:
        if p[2] == p[6] and p[4] == p[5] and p[5] == p[7]:
            c += 1
            print(p)

print('Palabras con las condiciones dadas:', c)
