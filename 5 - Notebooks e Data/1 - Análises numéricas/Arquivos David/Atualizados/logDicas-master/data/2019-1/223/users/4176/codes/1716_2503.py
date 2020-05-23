n = int(input("constante: "))
valor = 0

while (n >= 1):
	if (n%2 == 1):
		valor = valor + (4/(2*n-1))
	else:
		valor = valor - (4/(2*n-1))
		
	n = n-1
	
print(round(valor,8))
	
	