# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a = int(input("numero do dia de hoje: "))
b = int(input("dia futuro: "))
s = a+b
if (s=+6):
	y = s%7 
else:
	y = s
if (y == 0):
	y = "domingo"
elif (y ==1):
	y = "segunda"
elif (y == 2):
	y = "terca"
elif (y == 3):
	y = "quarta"
elif (y == 4):
	y = "quinta"
elif (y == 5):
	y = "sexta"
elif (y == 6):
	y = "sabado"

if not(0<=a<=6):
	print("A entrada", a, "eh invalida")
elif (a==0):
	x = "domingo"
	print("Hoje eh", x, "e o dia futuro eh", y)
elif (a ==1):
	x = "segunda"
	print("Hoje eh", x, "e o dia futuro eh", y)
elif (a == 2):
	x = "terca"
	print("Hoje eh", x, "e o dia futuro eh", y)
elif (a == 3):
	x = "quarta"
	print("Hoje eh", x, "e o dia futuro eh", y)
elif (a == 4):
	x = "quinta"
	print("Hoje eh", x, "e o dia futuro eh", y)
elif (a == 5):
	x = "sexta"
	print("Hoje eh", x, "e o dia futuro eh", y)
elif (a == 6):
	x = "sabado"
	print("Hoje eh", x, "e o dia futuro eh", y)