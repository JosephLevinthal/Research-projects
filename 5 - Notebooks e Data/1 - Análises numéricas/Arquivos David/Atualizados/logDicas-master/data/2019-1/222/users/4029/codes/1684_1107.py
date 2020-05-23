diaH = int(input("Numero referente ao dia de hoje na semana: "))

if (diaH == 0) or (diaH == 1) or (diaH == 2) or (diaH == 3) or (diaH == 4) or (diaH == 5) or (diaH == 6):
	diaF = int(input("Numero de dias no futuro a partir de hoje: "))
	if (diaF >= 0):
		# dia atual
		if (diaH == 0):
			msg = "Hoje eh domingo"
		if (diaH == 1):
			msg = "Hoje eh segunda"
		if (diaH == 2):
			msg = "Hoje eh terca"
		if (diaH == 3):
			msg = "Hoje eh quarta"
		if (diaH == 4):
			msg = "Hoje eh quinta"
		if (diaH == 5):
			msg  = "Hoje eh sexta"
		if (diaH == 6):
			msg = "Hoje eh sabado"
			
		# para descobrir o dia futuro
		if ((diaF % 7) + (diaH)) % 7 == 0:
			print(msg + " e o dia futuro eh domingo")
		if ((diaF % 7) + (diaH)) % 7 == 1:
			print(msg + " e o dia futuro eh segunda")
		if ((diaF % 7) + (diaH)) % 7 == 2:
			print(msg + " e o dia futuro eh terca")
		if ((diaF % 7) + (diaH)) % 7 == 3:
			print(msg + " e o dia futuro eh quarta")
		if ((diaF % 7) + (diaH)) % 7 == 4:
			print(msg + " e o dia futuro eh quinta")
		if ((diaF % 7) + (diaH)) % 7 == 5:
			print(msg + " e o dia futuro eh sexta")
		if ((diaF % 7) + (diaH)) % 7 == 6:
			print(msg + " e o dia futuro eh sabado")
	else:
		print("A entrada", diaF, "eh invalida")
else: 
	print("A entrada", diaH, "eh invalida")
