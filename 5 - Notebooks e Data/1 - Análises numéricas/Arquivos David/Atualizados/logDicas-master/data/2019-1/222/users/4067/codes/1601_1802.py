from math import*
#primeira entrada é os pontos de vida do boss
pontos = float(input("pontos de vida iniciais: "))
#lançamento do primeiro dado
d1 = float(input("valor 1: "))
#lançamento do segundo dado
d2 = float(input("valor 2: "))
#como resultado devo determinar os pontos de vida RESTANTES do boss
#o dano causado é dado por:
dano = (5**0.5*d1) + (pi*(d2//3))
print(int(pontos - dano))