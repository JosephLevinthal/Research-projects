x = int(input("Entre com o numero do dia de hoje: "))

if(0 > x) or (x > 6):
	print("A entrada ", x, " eh invalida")
	
y = int(input("Entre com o numero de dias apos hoje: "))

if(y >= 7):
	if(y % 7 != 0):
		dia_futuro = (x + (y % 7)) + 1
		if(dia_futuro > 6):
			dia_futuro = (dia_futuro - 6) - 1
	else:
		dia_futuro = x
else:
	dia_futuro = x + y
	if(dia_futuro > 6):
		dia_futuro = (dia_futuro - 6) - 1
		
if(x == 0):
	strx = "domingo"
elif(x == 1):
	strx = "segunda"
elif(x == 2):
	strx = "terca"
elif(x == 3):
	strx = "quarta"
elif(x == 4):
	strx = "quinta"
elif(x == 5):
	strx = "sexta"
else:
	strx = "sabado"
	
if(dia_futuro == 0):
	stry = "domingo"
elif(dia_futuro == 1):
	stry = "segunda"
elif(dia_futuro == 2):
	stry = "terca"
elif(dia_futuro == 3):
	stry = "quarta"
elif(dia_futuro == 4):
	stry = "quinta"
elif(dia_futuro == 5):
	stry = "sexta"
else:
	stry = "sabado"
	
print("Hoje eh ", strx, " e o dia futuro eh ", stry)