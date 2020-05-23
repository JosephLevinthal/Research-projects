# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = int(input("Digite aqui o dia referente a semana: "))
y = int(input("Digite aqui o dia futuro: "))
cal = (x + y) % 7
if (x >= 0) and (x <= 6):
	if (y > 0):
		if (x == 0):
			x = "domingo"
		elif (x == 1):
			x = "segunda"
		elif (x == 2):
			x = "terca"
		elif (x == 3):
			x = "quarta"
		elif (x == 4):
			x = "quinta"
		elif (x == 5):
			x = "sexta"
		elif (x == 6):
			x = "sabado"
		if (cal == 0):
			y = "domingo"
		elif (cal == 1):
			y = "segunda"
		elif (cal == 2):
			y = "terca"
		elif (cal == 3):
			y = "quarta"
		elif (cal == 4):
			y = "quinta"
		elif (cal == 5):
			y = "sexta"
		elif (cal == 6):
			y = "sabado"
		print("Hoje eh", x, "e o dia futuro eh", y)
	else:
		print("A entrada", y, "eh invalida")
else:
	print("A entrada", x, "eh invalida")