dia = int(input("Dia da semana:	"))

if(dia<0 or dia>6):
	print("A entrada",dia,"eh invalida")
else:
	fut = int(input("Dias no futuro:	"))
	if(dia+fut>6):
		X = (dia+fut)%7
	else:
		X = dia+fut

	if(X==0):
		X = "domingo"
	elif(X==1):
		X = "segunda"
	elif(X==2):
		X = "terca"
	elif(X==3):
		X = "quarta"
	elif(X==4):
		X = "quinta"
	elif(X==5):
		X = "sexta"
	elif(X==6):
		X = "sabado"
	
	if(dia == 0):
		dia = "domingo"
	elif(dia==1):
		dia = "segunda"
	elif(dia==2):
		dia = "terca"
	elif(dia==3):
		dia = "quarta"
	elif(dia==4):
		dia = "quinta"
	elif(dia==5):
		dia = "sexta"
	elif(dia==6):
		dia = "sabado"
		
	print("Hoje eh",dia,"e o dia futuro eh",X)