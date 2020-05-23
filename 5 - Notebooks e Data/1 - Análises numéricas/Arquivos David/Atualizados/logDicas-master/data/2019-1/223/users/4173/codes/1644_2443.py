from math import *
R = float(input("raio: "))
x = float(input("altura: "))
N = int(input("numero: "))

V1=4*pi*(R)**3/3
v2=(pi*x**2)*((3*R)-x)/3
be = (V1-v2)

if N==1 :
	mensagem = (v2)
else:
	mensagem = (be)
	
print(round(mensagem,4))

