dia1 = int(input("Entre com o numero do dia de hoje: "))
dia2 = int(input("Entre com o numero de dias apos hoje: "))
df = 0

if (dia1 <= 6) and (dia1 > 0): #checa se é um dia da semana
	if (dia1 + dia2 == 6):
		df = (dia1 + dia2)
		if df == 0:
			df = "domingo"
		elif df == 1:
			df = "segunda"
		elif df == 2:
			df = "terca"
		elif df == 3:
			df = "quarta"
		elif df == 4:
			df = "quinta"
		elif df == 5:
			df = "sexta"
		elif df == 6:
			df = "sabado"
	else:
		df = ((dia1 + dia2) % 7)
		if df == 0:
			df = "domingo"
		elif df == 1:
			df = "segunda"
		elif df == 2:
			df = "terca"
		elif df == 3:
			df = "quarta"
		elif df == 4:
			df = "quinta"
		elif df == 5:
			df = "sexta"
		elif df == 6:
			df = "sabado"
		
	if dia1 == 0:
		dh = "domingo"
		print("Hoje eh", dh, "e o dia futuro eh", df)
	if dia1 == 1:
		dh = "segunda"
		print("Hoje eh", dh, "e o dia futuro eh", df)
	if dia1 == 2:
		dh = "terca"
		print("Hoje eh", dh, "e o dia futuro eh", df)
	if dia1 == 3:
		dh = "quarta"
		print("Hoje eh", dh, "e o dia futuro eh", df)
	if dia1 == 4:
		dh = "quinta"
		print("Hoje eh", dh, "e o dia futuro eh", df)
	if dia1 == 5:
		dh = "sexta"
		print("Hoje eh", dh, "e o dia futuro eh", df)
	if dia1 == 6:
		dh = "sabado"
		print("Hoje eh", dh, "e o dia futuro eh", df)
else:
	print("A entrada", dia1, "eh invalida")