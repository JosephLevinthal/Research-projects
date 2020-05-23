q= int(input("Quantidade inicial: "))
pc= int(input("Percentual de Cres. Mensal: "))

meses= 0

while (0 < q < 8000):
	qprv= int(input("Quantidade de peixes retirados: "))
	q= q + ( q * (pc/100))
	q= q - qprv
	meses= meses + 1
	if (q <= 0):
		print("ZERO")
		
	elif (q >= 8000):
		print("MAXIMO")
		
print(meses)