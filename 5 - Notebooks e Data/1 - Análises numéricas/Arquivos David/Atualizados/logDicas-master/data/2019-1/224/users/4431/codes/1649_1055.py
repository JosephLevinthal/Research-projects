from math import*
v0=float(input("Digite a velocidade incial em m/s: "))
a=float(input("Digite o angulo em graus: "))
D=float(input("Digite a distancia horizontal entre o passaro e o porco: "))
a=radians(a)
R=(v0**2)*(sin(2*a))/9.8
R=abs(R)
if((D-R)<0.1):
	print("sim")
else:
	print("nao")
