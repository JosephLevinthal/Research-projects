from numpy import *
a = float(input("Aceleracao do carro: "))
v0 = float(input("Velocidade inicial do carro: "))
n = int(input("Digite um numero inteiro: "))

t = arange(n)
d = ((a * t**2)/2) + v0 * t
print(d)

