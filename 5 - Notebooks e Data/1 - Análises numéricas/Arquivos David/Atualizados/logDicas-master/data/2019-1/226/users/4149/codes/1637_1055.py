from math import *
vel=float(input("entre com a  velocidade inicial: "))
ang=float(input("entre com o valor do angulo: "))
d=float(input("entre com a distancia: "))
g=9.8
r=((vel**2)*sin(radians(2*ang)))/g



if(abs(d-r<= 0.1)):
	
	print("sim")
	
else:
	print("nao")