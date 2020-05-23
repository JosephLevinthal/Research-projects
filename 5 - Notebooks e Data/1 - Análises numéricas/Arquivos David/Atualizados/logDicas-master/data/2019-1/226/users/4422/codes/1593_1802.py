from math import *
vidainicial = int(input("Vida inicial: "))
d1 = int(input("Valor lancamento 1: "))
d2 = int(input("Valor lancamento 2: "))
dano = (sqrt(5 * d1) + pi ** (d2/3))
vidarestante = vidainicial - int(dano)
print(int(vidarestante))
