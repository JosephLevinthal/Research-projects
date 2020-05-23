from math import*
vida = int(input('Vida do monstro:'))
D1 = int(input('Dado 1:'))
D2 = int(input('Dado 2:'))
dano = int(sqrt(5*D1)+pi**(D2/3))
vidatotal = vida - dano
print(int(vidatotal))
