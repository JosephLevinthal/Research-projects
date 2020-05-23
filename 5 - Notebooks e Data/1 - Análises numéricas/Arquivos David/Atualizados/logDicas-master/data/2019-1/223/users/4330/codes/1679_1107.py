# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

hoje = int(input("sendo domingo igual 0, digite um numere para hoje:"))
futuro = int(input("digite um numero para dias futuros:"))

fut = (futuro + hoje) % 7

if(hoje != 0 and hoje != 1 and hoje != 2 and hoje != 3 and hoje != 4 and hoje != 5 and hoje != 6):
	print("A entrada",hoje,"eh invalida")

elif(hoje == 0):
	dia = "domingo"
	if (fut == 0):
		fut = "domingo"
	elif fut == 1:
		fut = "segunda"
	elif(fut == 2):
		fut = "terca"
	elif(fut == 3):
		fut = "quarta"
	elif(fut == 4):
		fut = "quinta"
	elif(fut == 5):
		fut = "sexta"
	elif(fut == 6):
		fut = "sabado"
		
elif(hoje == 1):
	dia = "segunda"
	if (fut == 0):
		fut = "domingo"
	elif fut == 1:
		fut = "segunda"
	elif(fut == 2):
		fut = "terca"
	elif(fut == 3):
		fut = "quarta"
	elif(fut == 4):
		fut = "quinta"
	elif(fut == 5):
		fut = "sexta"
	elif(fut == 6):
		fut = "sabado"
	
elif(hoje == 2):
	dia = "terca"
	if (fut == 0):
		fut = "domingo"
	elif fut == 1:
		fut = "segunda"
	elif(fut == 2):
		fut = "terca"
	elif(fut == 3):
		fut = "quarta"
	elif(fut == 4):
		fut = "quinta"
	elif(fut == 5):
		fut = "sexta"
	elif(fut == 6):
		fut = "sabado"
		
elif(hoje == 3):
	dia = "quarta"
	if (fut == 0):
		fut = "domingo"
	elif fut == 1:
		fut = "segunda"
	elif(fut == 2):
		fut = "terca"
	elif(fut == 3):
		fut = "quarta"
	elif(fut == 4):
		fut = "quinta"
	elif(fut == 5):
		fut = "sexta"
	elif(fut == 6):
		fut = "sabado"
	
elif(hoje == 4):
	dia = "quinta"
	if (fut == 0):
		fut = "domingo"
	elif fut == 1:
		fut = "segunda"
	elif(fut == 2):
		fut = "terca"
	elif(fut == 3):
		fut = "quarta"
	elif(fut == 4):
		fut = "quinta"
	elif(fut == 5):
		fut = "sexta"
	elif(fut == 6):
		fut = "sabado"
		
elif(hoje == 5):
	dia = "sexta"
	if (fut == 0):
		fut = "domingo"
	elif fut == 1:
		fut = "segunda"
	elif(fut == 2):
		fut = "terca"
	elif(fut == 3):
		fut = "quarta"
	elif(fut == 4):
		fut = "quinta"
	elif(fut == 5):
		fut = "sexta"
	elif(fut == 6):
		fut = "sabado"
		
elif(hoje == 6):
	dia = "sabado"
	if (fut == 0):
		fut = "domingo"
	elif fut == 1:
		fut = "segunda"
	elif(fut == 2):
		fut = "terca"
	elif(fut == 3):
		fut = "quarta"
	elif(fut == 4):
		fut = "quinta"
	elif(fut == 5):
		fut = "sexta"
	elif(fut == 6):
		fut = "sabado"
	print("Hoje eh",dia,"e o dia futuro eh",fut)
