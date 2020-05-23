from math import factorial
# Leitura do numero de pessoas
n = float(input("Digite o numero de pessoas: "))
# Calculo da probabilidade de dois aniversariantes no mesmo dia
p = 1 - ((factorial(365)/factorial(365 - n)) * (1/365**n))

print(round(p*100, 2))
