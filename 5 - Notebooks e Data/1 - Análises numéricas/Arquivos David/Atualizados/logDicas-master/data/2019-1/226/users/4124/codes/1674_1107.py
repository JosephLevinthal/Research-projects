# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = int(input("Numero do dia de hoje: "))
y = int(input("Numero de dias depois de hoje: "))
z = (x + y) % 7
if(x >= 0 and x <= 6):
	if(x >= 0):
		if(x == 0):
			x = "domingo"
		elif(x == 1):
			x = "segunda"
		elif(x == 2):
			x = "terca"
		elif(x == 3):
			x = "quarta"
		elif(x == 4):
			x = "quinta"
		elif(x == 5):
			x = "sexta"
		elif(x == 6):
			x = "sabado"
		if(z == 0):
			y = "domingo"
		elif(z == 1):
			y = "segunda"
		elif(z == 2):
			y = "terca"
		elif(z == 3):
			y = "quarta"
		elif(z == 4):
			y = "quinta"
		elif(z == 5):
			y = "sexta"
		elif(z == 6):
			y = "sabado"
		print("Hoje eh", x, "e o dia futuro eh", y,)
else:
		print("A entrada", x, "eh invalida")
		

	
