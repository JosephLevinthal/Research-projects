# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

n = int(input("hje:"))

if(n>6 and n<0):
	print("A entrada", n, "eh invalida")
else:
	df = int(input("Dias futuros: "))
	df = df + n
	if(df>7):
		
		df = df%6
		df = df +1
	else:
		df = df -1
	
		
	if(n == 0):
		hj = "domingo"
	elif(n == 1):
		hj = "segunda"
	elif(n == 2):
		hj = "terca"
	elif(n == 3):
		hj = "quarta"
	elif(n == 4):
		hj = "quinta"
	elif(n == 5):
		hj = "sexta"
	elif(n == 6):
		hj = "sabado"
	msg = "Hoje eh "+hj
	n = df
	if(n == 0):
		hj = "domingo"
	elif(n == 1):
		hj = "segunda"
	elif(n == 2):
		hj = "terca"
	elif(n == 3):
		hj = "quarta"
	elif(n == 4):
		hj = "quinta"
	elif(n == 5):
		hj = "sexta"
	elif(n == 6):
		hj = "sabado"
	msg = msg+" e o dia futuro eh "+hj
	print(msg)
		
		