'''import random

def get_ganador(usuario, compu):
    if usuario == compu:
        return 'empate'
    elif (usuario == 0 and compu == 2) or (usuario == 1 and compu == 0) or (usuario == 2 and compu == 1):
        return 'usuario'
    else:
        return 'compu'

opciones = {0: 'piedra', 1: 'papel', 2: 'tijeras'}
# El usuario elige su opción
print('0: piedra')
print('1: papel')
print('2: tijeras')
usuario = int(input('Escribe tu opción: '))
# La computadora elige
compu = random.choice([0, 1, 2])

print('Usted seleccionó:', opciones[usuario])
print('La computadora seleccionó:', opciones[compu])
gana = get_ganador(usuario, compu)
print('Y el ganador es:', gana)



import random

def get_ganador2(usuario, compu):
   if ((usuario - compu)%3) == 0:
	return 'empate'
   elif ((usuario - compu)%3) ==  1:
	return 'usuario'
   else:
	return 'compu'	

opciones = {0: 'piedra', 1: 'papel', 2: 'tijeras'}
# El usuario elige su opción
print('0: piedra')
print('1: papel')
print('2: tijeras')
usuario = int(input('Escribe tu opción: '))
# La computadora elige
compu = random.choice([0, 1, 2])

print('Usted seleccionó:', opciones[usuario])
print('La computadora seleccionó:', opciones[compu])
gana = get_ganador(usuario, compu)
print('Y el ganador es:', gana)'''








import random
   
def get_ganador2(usuario, compu):
    if (usuario - compu) == 0:
        return 'empate'
    elif ((usuario - compu)%5) == 1 or (usuario - compu)%5 == 2:
        return 'usuario'
    else:
        return 'compu'
        
opciones = {0:'piedra',1:'Spock',2:'papel',3:'lagarto',4:'tijeras'}
# el usuario da su opción
print('0:piedra')
print('1:Spock')
print('2:papel')
print('3:lagarto')
print('4:tijeras')
usuario = int(input('escriba su opción:'))
# la computadora escoje
compu = random.choice([0,1,2,3,4])
print('usted seleccionó: ',opciones[usuario])
print('la compu seleccionó: ',opciones[compu])
gana = get_ganador2(usuario, compu)
print('y el ganador es:', gana)