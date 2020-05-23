escala = input("Celsius ou Fahrenheit? (c/F)  ")
temp = float(input("Temperatura: "))

F = temp*(9/5) + 32
C = (5/9)*(temp - 32)

if (escala.lower() == "c"):
	print(round(F,4))
	
if(escala.upper() == "F"):
	print(round(C,4))