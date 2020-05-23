# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
day = int(input("dia: (0 a 6) "))
future = int(input("dia(s) futuro(s): "))

if (day < 0) or (day > 6):
	solution = 7
elif ((day + future) < 7):
	solution = day + future
else:
	solution = ((day + future) % 7)

if solution == 0:
	especific = "domingo"
elif solution == 1:
	especific = "segunda"
elif solution == 2:
	especific = "terca"
elif solution == 3:
	especific = "quarta"
elif solution == 4:
	especific = "quinta"
elif solution == 5:
	especific = "sexta"
elif solution == 6:
	especific = "sabado"
else:
	especific = "inexistente"
	
if day == 0:
	dia = "domingo"
elif day == 1:
	dia = "segunda"
elif day == 2:
	dia = "terca"
elif day == 3:
	dia = "quarta"
elif day == 4:
	dia = "quinta"
elif day == 5:
	dia = "sexta"
else:
	dia = "sabado"
	
if (day < 0) or (day > 6):
	print("A entrada", day, "eh invalida")
else:
	print("Hoje eh",dia, "e o dia futuro eh",especific)
	