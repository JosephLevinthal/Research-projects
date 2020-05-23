from math import*

velocidade0= float(input("v0: "))
angulo= radians(float(input("Ângulo: ")))
distancia= float(input("Distancia: "))

g= 9.8
formula= ((velocidade0**2)*sin(2*angulo))/g
	 
if (abs(formula - distancia)) <= 0.1:
	 print("sim")

else:
	 print("nao")