from math import *
life = int(input(" pontos de vida iniciais "))
D1 = int(input(" primeiro numero em que parou o dado "))
D2 = int(input(" segundo numero em que parou o dado "))
dano = (sqrt(5 * D1) + pi * D2/3)
print( life - dano )