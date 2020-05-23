# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = int(input("Insira o numero: "))
y = int(input("Insira o dia futuro: "))
f = (x + y) % 7

if(x > 6 or x < 0):
	print("A entrada", x,"eh invalida")
else:
	if(x == 0):
		msg = "Hoje eh domingo"
	elif(x == 1):
		msg = "Hoje eh segunda"
	elif(x == 2):
		msg = "Hoje eh terca"
	elif(x == 3):
		msg = "Hoje eh quarta"
	elif(x == 4):
		msg = "Hoje eh quinta"
	elif(x == 5):
		msg = "Hoje eh sexta"
	elif(x == 6):
		msg = "Hoje eh sabado"

if(f == 0):
	msg2 = "e o dia futuro eh domingo"
elif(f == 1):
	msg2 = "e o dia futuro eh segunda"
elif(f == 2):
	msg2 = "e o dia futuro eh terca"
elif(f == 3):
	msg2 = "e o dia futuro eh quarta"
elif(f == 4):
	msg2 = "e o dia futuro eh quinta"
elif(f == 5):
	msg2 = "e o dia futuro eh sexta"
elif(f == 6):
	msg2 = "e o dia futuro eh sabado"

if(x <= 6 and x >= 0):
	print(msg, msg2)