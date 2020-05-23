d = int(input("qual o dia? "))
if ((d >= 0 and d <= 6)):
	j = int(input("quantos dias: "))
	d1 = (d+j)%7
	if (d == 0):
		d = "domingo"
	elif (d == 1):
		d = "segunda"
	elif (d == 2):
		d = "terca"
	elif (d == 3):
		d = "quarta"
	elif (d == 4):
		d = "quinta"
	elif (d == 5):
		d = "sexta"
	else:
		d = "sabado"
	if (d1 == 0):
		d1 = "domingo"
	elif (d1 == 1):
		d1 = "segunda"
	elif (d1 == 2):
	   d1 = "terca"
	elif (d1 == 3):
		d1 = "quarta"
	elif (d1 == 4):
		d1 = "quinta"
	elif (d1 == 5):
		d1 = "sexta"
		d1 = "sabado"
	print("Hoje eh",d,"e o dia futuro eh",d1)
else:
	print("A entrada",d,"eh invalida")