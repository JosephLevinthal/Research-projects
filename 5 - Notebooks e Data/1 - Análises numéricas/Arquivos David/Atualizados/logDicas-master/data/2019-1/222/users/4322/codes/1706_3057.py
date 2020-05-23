tempo = float(input("quanto tempo durou? "))
if((tempo >= 0) and (tempo <= 100)):
	valor = tempo * 80.00 + 3000.00
	print(round(valor, 2))
elif((tempo > 100) and ( tempo <= 200)):
	valor = tempo * 90.00 + 4000.00
	print(round(valor, 2))
elif((tempo > 200) and (tempo <= 300)):
	valor = tempo * 100.00 + 5000.00
	print(round(valor, 2))
elif((tempo > 300)):
	valor = tempo * 110 + 6000.00
	print(round(valor, 2))