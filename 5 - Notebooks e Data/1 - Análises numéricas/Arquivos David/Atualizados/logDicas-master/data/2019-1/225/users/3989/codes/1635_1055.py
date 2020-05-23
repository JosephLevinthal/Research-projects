from math import* 
Vo = float(input("Digite vo: "))
alpha = radians(float(input("Digite alpha:")))
d = float(input("digite distância: "))
			  
g = 9.8 
R = (Vo ** 2 * sin (2*alpha))/g

if(abs(d - R)< 0.1):
	print("sim")
else:
	print("nao")

				

