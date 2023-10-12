import random   #importamos un random para aleatorizar las plabaras de abajo
palabras = [
    'computadora', 'manzana', 'pera', 'naranja', 'teclado', 'sol', 'verde', 'azul',
    'audifonos', 'correr', 'volar', 'avion', 'casa', 'pasto', 'tacos', 'alfabeto',
    'tarea', 'diseño', 'algoritmos', 'libro', 'morado', 'luna', 'diamante', 'rapido',
    'carro', 'moto', 'bicicleta', 'agua', 'fuego', 'lava', 'pizarron', 'tele',  #lista de palabras 
    'pantalla', 'tienda', 'colchon', 'sillon', 'lampara', 'pluma', 'lapiz', #que aleatorizaremos
    'lapicera', 'botella', 'caja', 'rollo', 'puerta', 'suelo', 'tierra', 'ola',
    'corazon', 'pila', 'cristal', 'vidrio', 'metal', 'viga', 'ladrillo', 'planta'
]

def crenglon (words, cantidad_palabras):       #definimos crenglon
    renglon = random.sample(words, cantidad_palabras)   #creamos un renglon de palabras en españo
    return ' '.join(renglon)
renglon1 = crenglon(palabras, 30)                   #creamos 2 renglones de 30 palabras 
renglon2 = crenglon(palabras, 30)
with open('palabras.txt', 'w', encoding='utf-8') as archivo:    #usamos la funcion write para escribir
    archivo.write(renglon1 + '\n')                              #los renglones en palabras.txt
    archivo.write(renglon2 + '\n')

