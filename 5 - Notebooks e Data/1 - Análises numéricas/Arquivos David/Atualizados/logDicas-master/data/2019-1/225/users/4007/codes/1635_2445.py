escala = input("escala (C/F): ")
temperatura = float(input("temperatura: "))

if (escala == "C"):
	temperatura = 9/5 * (temperatura) + 32
	
else: 
	temperatura = 5/9 * (temperatura - 32)
	

	
print(round(temperatura, 2))
	
   


