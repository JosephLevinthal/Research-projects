x = int(input("numero inteiro: "))
y = int(input("numero do dia no futuro: "))

#caluclo do y 
c = (x + y) % 7

if(x >= 0 and x <= 6):
	if(y > 0):
		if(x == 0):
			z = "domingo" 
		elif(x == 1):
			z = "segunda" 
		elif(x == 2):
			z = "terca" 
		elif(x == 3):
			z = "quarta" 
		elif(x == 4):
			z = "quinta"
		elif(x == 5):
			z = "sexta" 
		elif(x == 6):
			z = "sabado" 
		if(c == 0):
			p = "domingo"
		elif(c == 1):
			p = "segunda"
		elif(c == 2):
			p = "terca"
		elif(c == 3):
			p = "quarta"
		elif(c == 4):
			p = "quinta"
		elif(c == 5):
			p = "sexta"
		elif(c == 6):
			p = "sabado"
		print("Hoje eh", z, "e o dia futuro eh", p)
	else:
		print("A entrada", y, "eh invalida")
else:
	print("A entrada", x, "eh invalida")
	
