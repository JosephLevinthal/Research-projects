from math import*

raio= float(input("Raio do tanque: "))
altura=float(input("Altura x: "))

opc= int(input(" 1 ou 2: "))

if (opc == 2):
	formula=((pi*altura**2)*(3*raio - altura))
	print(round(formula,4))
	
else:
	print(formula - (4*pi*raio**3)/3)


                                                                                                                        