import math


prato = float(input("Gramas do prato: "))
bebidas = int(input("Bebidas: "))
sobremesas = int(input("Sobremesas: "))
PP = 26.90
PB = 3.50
PS = 3
total = (prato/1000)*(PP)+(bebidas*PB)+(sobremesas*PS)

print(round(total, 2))