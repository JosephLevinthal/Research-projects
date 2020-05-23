a = int(input("Dia: "))
b = int(input("Futuro: "))

c = (a + b)%7

if (a >= 0) and (a <= 6):
	if (b > 0):
		if (a == 0):
			x = "domingo"
		elif (a == 1):
			x = "segunda"
		elif (a == 2):
			x = "terca"
		elif (a == 3):
			x = "quarta"
		elif (a == 4):
			x = "quinta"
		elif (a == 5):
			x = "sexta"
		elif (a == 6):
			x = "sabado"
		if (c == 0):
			y = "domingo"
		elif (c == 1):
			y = "segunda"
		elif (c == 2):
			y = "terca"
		elif (c == 3):
			y = "quarta"
		elif (c == 4):
			y = "quinta"
		elif (c == 5):
			y = "sexta"
		elif (c == 6):
			y = "sabado"
		print("Hoje eh", x, "e o dia futuro eh", y)
	else:
		print("A entrada", b, "eh invalida")
else:
	print("A entrada", a, "eh invalida")
	
			