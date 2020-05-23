QIP = int(input("Quantidade inicial: "))
PC = float(input("Insira o Perc: "))

A = QIP
cont = 0


while (A > 0 and A < 8000):
	RET = int(input("Quantos sao retirados: "))
	A = A + ((A*PC)/100)
	A = A - RET
	cont = cont + 1
if (A <= 0):
	print("ZERO")
	print(cont)
else:
	print("MAXIMO")
	print(cont)
	
	