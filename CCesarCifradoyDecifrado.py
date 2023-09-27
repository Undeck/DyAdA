#Cifrado cesar 
'''def cifraCesar (cad, key):
    cifrado = ""
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    cad = cad.lower() 
    for c in cad:
        if c in alfabeto:
         pos = alfabeto.index(c)
         cifrado = cifrado + alfabeto [(pos + key)%27]
        else:
           cifrado += c
    return cifrado

print(cifraCesar('hola mundo', 50))'''

#Cifrado cesar 
def cifraCesar (cad, key):
    cifrado = ""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    cad = cad.lower() 
    for c in cad:
        if c in alfabeto:
         pos = alfabeto.index(c)
         cifrado = cifrado + alfabeto [(pos + key)%len(alfabeto)]
        else:
           cifrado += c
    return cifrado

    
#Decifrado cesar 
def decifraCesar (cad, key):
    decifrado = ""
    alfabeto = 'abcdefghijklmnnopqrstuvwxyz'
    cad = cad.lower() 
    for c in cad:
        if c in alfabeto:
         pos = alfabeto.index(c)
         decifrado = decifrado + alfabeto [(pos - key)%len(alfabeto)]
        else:
           decifrado += c
    return decifrado
a = 'a zsnw dwsjfwv lzsl hwghdw oadd xgjywl ozsl qgm ksav, hwghdw oadd xgjywl ozsl qgm vav, tml hwghdw oadd fwnwj xgjywl zgo qgm esvw lzwe xwwd. - esqs sfywdgm.  a slljatmlw eq kmuuwkk lg lzak: a fwnwj ysnw gj lggc sfq wpumkw. xdgjwfuw fayzlafysdw.  lzw twkl laew lg hdsfl s ljww osk 20 qwsjk syg. lzw kwugfv twkl laew ak fgo. uzafwkw hjgnwjt. a se fgl s hjgvmul gx eq uajumeklsfuwk. a se s hjgvmul gx eq vwuakagfk. klwhzwf ugnwq. uzsfyw qgmj lzgmyzlk sfv qgm uzsfyw qgmj ogjdv. fgjesf nafuwfl hwsdw'
b = cifraCesar(a,8)
print (b)
print (decifraCesar(b,8))

'''for llave in range(26):
   print(decifraCesar(a,llave),llave)'''      #Sirve para ver las posibles combinaciones