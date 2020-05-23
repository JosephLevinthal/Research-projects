x = int(input("Digite o dia da semana: "))
if (x > 6):
	print("A entrada", x, "eh invalida")
else:
	y = int(input("Digite daqui a quantos dias: "))
	dia = ( y % 7 )
	dia = dia + x
	dia = ( dia % 7)
	if(dia == 0):
		Dia = "domingo"
	elif(dia == 1):
		Dia = "segunda"
	elif(dia == 2):
		Dia = "terca"
	elif(dia == 3):
		Dia = "quarta"
	elif(dia == 4):
		Dia = "quinta"
	elif(dia == 5):
		Dia = "sexta"
	elif(dia == 6):
		Dia = "sabado"

	if(x == 0):
		d = "domingo"
	elif(x == 1):
		d = "segunda"
	elif(x == 2):
		d = "terca"
	elif(x == 3):
		d = "quarta"
	elif(x == 4):
		d = "quinta"
	elif(dia == 5):
		d = "sexta"
	elif(x == 6):
		d = "sabado"
	print("Hoje eh", d, "e o dia futuro eh", Dia)
			

		
		
	

	