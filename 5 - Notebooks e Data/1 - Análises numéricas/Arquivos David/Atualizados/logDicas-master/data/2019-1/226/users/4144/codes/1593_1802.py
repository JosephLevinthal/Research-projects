from math import*
pm = int(input("pontos do monstro: "))
d1 = int(input("dado1: "))
d2 = int(input("dado2: "))
dano = int(abs(sqrt(5 * d1) +  pi ** (d2 /3)))
virest = (pm - dano)
print(virest)