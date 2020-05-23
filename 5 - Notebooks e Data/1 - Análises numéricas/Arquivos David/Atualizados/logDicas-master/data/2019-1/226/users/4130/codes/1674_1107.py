a = int(input("Dia de hoje:"))
b = int(input("Numero de dias apos hoje:"))
		  
x = "Hoje eh "
y = " e o dia futuro eh "
		  
c = (a + b) % 7
		  
if(a == 0):
	a = "domingo"
	if(c == 0):
		  c = "domingo"
	elif(c == 1):
		  c = "segunda"
	elif(c == 2):
		  c = "terca"
	elif(c == 3):
		  c = "quarta"
	elif(c == 4):
		  c = "quinta"
	elif(c == 5):
		  c = "sexta"
	elif(c == 6):
		  c = "sabado"
	print(x, a, y, c)
elif(a == 1):
	a = "segunda"
	if(c == 0):
		  c = "domingo"
	elif(c == 1):
		  c = "segunda"
	elif(c == 2):
		  c = "terca"
	elif(c == 3):
		  c = "quarta"
	elif(c == 4):
		  c = "quinta"
	elif(c == 5):
		  c = "sexta"
	elif(c == 6):
		  c = "sabado"
	print(x, a, y, c)
elif(a == 2):
	a = "terca"
	if(c == 0):
		  c = "domingo"
	elif(c == 1):
		  c = "segunda"
	elif(c == 2):
		  c = "terca"
	elif(c == 3):
		  c = "quarta"
	elif(c == 4):
		  c = "quinta"
	elif(c == 5):
		  c = "sexta"
	elif(c == 6):
		  c = "sabado"
	print(x, a, y, c)
elif(a == 3):
	a = "quarta"
	if(c == 0):
		  c = "domingo"
	elif(c == 1):
		  c = "segunda"
	elif(c == 2):
		  c = "terca"
	elif(c == 3):
		  c = "quarta"
	elif(c == 4):
		  c = "quinta"
	elif(c == 5):
		  c = "sexta"
	elif(c == 6):
		  c = "sabado"
	print(x, a, y, c)
elif(a == 4):
	a = "quinta"
	if(c == 0):
		  c = "domingo"
	elif(c == 1):
		  c = "segunda"
	elif(c == 2):
		  c = "terca"
	elif(c == 3):
		  c = "quarta"
	elif(c == 4):
		  c = "quinta"
	elif(c == 5):
		  c = "sexta"
	elif(c == 6):
		  c = "sabado"
	print(x, a, y, c)
elif(a == 5):
	a = "sexta"
	if(c == 0):
		  c = "domingo"
	elif(c == 1):
		  c = "segunda"
	elif(c == 2):
		  c = "terca"
	elif(c == 3):
		  c = "quarta"
	elif(c == 4):
		  c = "quinta"
	elif(c == 5):
		  c = "sexta"
	elif(c == 6):
		  c = "sabado"
	print(x, a, y, c)
elif(a == 6):
	a = "sabado"
	if(c == 0):
		  c = "domingo"
	elif(c == 1):
		  c = "segunda"
	elif(c == 2):
		  c = "terca"
	elif(c == 3):
		  c = "quarta"
	elif(c == 4):
		  c = "quinta"
	elif(c == 5):
		  c = "sexta"
	elif(c == 6):
		  c = "sabado"
	print(x, a, y, c)
else:
	print("A entrada",a," eh invalida")