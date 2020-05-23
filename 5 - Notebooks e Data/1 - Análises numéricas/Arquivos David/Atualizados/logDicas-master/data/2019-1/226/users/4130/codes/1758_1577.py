from numpy import *

acel = float(input("Digite a distancia: "))
veloc = float(input("Digite a velocidade: "))
n = int(input("Digite um numero: "))

t = arange(n)
d = zeros(n, dtype = int)

d = ((acel * t ** 2) / 2) + veloc * t

print(d)