from math import*
Pv = int(input("pontos de vida iniciais: "))
V = int(input("valores D1: "))
vo = int(input("valor D2: "))

dano = sqrt(5*V)+(pi**(vo/3))
f= Pv - int(dano)
print(f)