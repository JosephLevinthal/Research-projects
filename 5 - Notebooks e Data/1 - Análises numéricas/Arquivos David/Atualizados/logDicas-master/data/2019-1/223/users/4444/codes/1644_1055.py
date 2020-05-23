from math import * 


#Leitura dos valores
v0 = float(input("Digite a v0: "))
a = float(input("Digite o angulo do vetor de lancamento: "))
D = float(input("Digite a distancia em metros entre o passaro e o porco: "))
rad = radians(a)
Ra = v0**2
Rb = sin(2 * rad)
g = 9.8
R = (Ra * Rb)/g
dif = abs(D - R)
dif = round(dif, 2)

if(dif <= 0.1):
	print("sim")

else:
	print("nao")