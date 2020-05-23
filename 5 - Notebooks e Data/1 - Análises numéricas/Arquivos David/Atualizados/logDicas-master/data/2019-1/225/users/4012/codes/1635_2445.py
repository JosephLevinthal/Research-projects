escala = input("escala? (C/F): ")
valor = float(input("digite temp: "))

if (escala == "C"):
	temp = (9 / 5 * valor) + 32
else:
	temp = 5 / 9 * (valor - 32)
	
print(round(temp, 2))
	

