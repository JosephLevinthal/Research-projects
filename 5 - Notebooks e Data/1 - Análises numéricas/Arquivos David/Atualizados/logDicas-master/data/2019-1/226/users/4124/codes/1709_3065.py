tipo = input("Tipo de ataque: ").upper()
n = int(input("Valor do dado: "))
trn = int(input("Numero de turnos: "))

if((tipo == "CAUDA" or tipo == "CUSPE" or tipo == "PATADA") and (n >= 1 and n <= 4)):
	if(tipo == "CAUDA"):
		pv = n * trn
		print(pv)
	elif(tipo == "CUSPE"):
		pv = 2 * n * trn
		print(pv)
	elif(tipo == "PATADA"):
		pv = ((2 * n) - 5) * trn
		print(pv)
else:
	print("Entrada invalida")