'''import random

def alfabeto_aleatorio (alfabeto):
    alfabeto2 = ""

    while len (alfabeto2)<26:
        ale = random.choice(alfabeto)
        if not ale in alfabeto2:
            alfabeto2 += ale
    return alfabeto2

def alfabeto_aleatorio2 (alfabeto3):
    random.shuffle (alfabeto3)
    return alfabeto3
    
    def  carga_palabras():
    dic = carga_palabras(words2.txt)
    Texto = "I pqr r yevrz qvvxvdq. Od selqrt rszvedood I slslupvq goex rz 5 ai . I gvdz poiv rdq zoox r upogue zpvd I gvdz zo uvv r kocabv os it slevdqu rz r hre gogdzogd" 
    '''


texto = "I pqr r yevrz qvvxvdq. Od selqrt rszvedood I slslupvq goex rz 5 ai . I gvdz poiv rdq zoox r upogue zpvd I gvdz zo uvv r kocabv os it slevdqu rz r hre gogdzogd"
'''b = cifraSustitucion(texto, miAlfabeto)
print(b)'''
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
frecuencia = {}
for c in alfabeto:
    frecuencia[c] = 0
#print (frecuencia)
for e in texto: #a
    if e in alfabeto:
        frecuencia[e]+=1
print(frecuencia)

def cargaPalabras():
    archivo = open ('words2.txt', 'r')
    renglon = archivo.readline()
    palabras = renglon.split()
    print (len(palabras), 'palabras leidas')
    return palabras
dic = cargaPalabras('words2.txt')
c = 0 
for p in dic:
    if len(p) == 8:
        if p ([2]==p[6]) and (p[1]==p[5]) and (p[5]==p[7]):
            c=c+1
            print(p)
print(c)