from math import*
v0=float(input("velocidade inicial: "))
an=float(input("angulo: "))
d=float(input("distancia entre o passaro e o porco: "))
g=9.8
an=radians(an)
r=((v0)**2 * sin(2*an))/g

if abs(d-r<= 0.1):
	mensagem="sim"
else:
	mensagem="nao"
print(mensagem)
