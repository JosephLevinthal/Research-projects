from math import*


v0 = float(input("velocidade: "))
a = float(input("angulo: "))
d = float(input("distancia: "))

r = (v0**2) * (sin(2*(radians(a)))) / 9.8

D = abs(r - d)

if ( D < 0.1):
	mensagem = "sim"
else:
	mensagem = "nao"

print(mensagem)
