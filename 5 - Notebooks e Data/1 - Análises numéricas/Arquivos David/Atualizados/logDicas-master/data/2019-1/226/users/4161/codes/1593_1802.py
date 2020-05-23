from math import * 

vida = int(input("vida do monstro: "))
d1 = int(input("valor dado 1: "))
d2 = int(input("valor dado 2: "))

f = abs(sqrt( 5 * d1 ) + pi ** (d2 / 3)) 
dano = int(f)
print(vida - dano)
