resultado = input("Resultado da partida: ").lower()

V = 3
E = 1
D = 0
cont = 0

while (resultado != "V" or "E" or "D"):
	if (resultado == "V"):
		cont = V
		elif (resultado == "E"):
			cont = E
		elif (resultado == "D"):
			cont = D
			
print(cont + cont)
		
	
	
