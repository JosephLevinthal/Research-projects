from numpy import *

frase  = input("Digite uma frase: ")
 
frase = frase.replace(" ","").upper()
print (frase)


# Verifica se a frase e ou nao palindroma
qtdeLetras = len(frase)

normal = frase[0:qtdeLetras]
inverso = frase[qtdeLetras::-1]

if normal == inverso :
    print (1)
else:
    print (0)