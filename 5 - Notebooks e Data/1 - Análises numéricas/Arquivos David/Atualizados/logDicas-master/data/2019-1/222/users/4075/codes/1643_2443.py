from math import *
a=float(input("leia o raio:"))
h=float(input("leia a altura"))
n=int(input("leia a opcao desejada/n1 - volume de ar/t2 - volume do combustivel:"))
vr=(4*pi*a*a*a)/3
v=((pi*h*h))*((3*a-h))/3
vcom= vr-v
if(n==1):
	print(round(v,4))
else:
	print(round(vcom,4))