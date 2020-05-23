from math import*
vida = float(input('digite vida: '))
D1 = float(input('digite D1: '))
D2 = float(input('digite D2: '))

dano = (((D1*5)**(0.5)) + pi**(D2/3)) // 1

resultado = vida - dano

print(resultado)