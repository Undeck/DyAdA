import random
palabras = [
    'casa', 'perro', 'gato', 'sol', 'luna', 'amigo', 'amarillo', 'jugar',
    'comer', 'manzana', 'cielo', 'tierra', 'flor', 'agua', 'montaña', 'ciudad',
    'carro', 'viaje', 'canción', 'libro', 'verde', 'rojo', 'niño', 'niña',
    'escuela', 'trabajo', 'familia', 'amor', 'correr', 'nadar', 'nube', 'ventana',
    'puerta', 'televisión', 'computadora', 'musica', 'pintura', 'bailar', 'dormir',
    'despertar', 'invierno', 'verano', 'primavera', 'otoño', 'corazón', 'pensar',
    'soñar', 'risa', 'lluvia', 'viento', 'dulce', 'amable', 'sonrisa', 'abrazo',
    'beso', 'silencio', 'viajar', 'caminar', 'volar', 'navegar', 'planeta', 'estrella'
]

def crenglon (words, cantidad_palabras):
    renglon = random.sample(words, cantidad_palabras)
    return ' '.join(renglon)
renglon1 = crenglon(palabras, 30)
renglon2 = crenglon(palabras, 30)
with open('palabras.txt', 'w', encoding='utf-8') as archivo:
    archivo.write(renglon1 + '\n')
    archivo.write(renglon2 + '\n')

print("Diccionario guardado en 'palabras.txt'.")

