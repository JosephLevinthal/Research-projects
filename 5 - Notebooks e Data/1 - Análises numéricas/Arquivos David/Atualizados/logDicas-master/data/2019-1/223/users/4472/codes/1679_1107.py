dia = int(input("Dia da Semana: "))
futuro = int(input("Dias a contar: "))
soma = (dia + futuro) % 7

if dia < 0 and dia > 6:
	print ("A entrada",dia,"eh invalida")
	
# Dia 0 - Domingo
elif dia == 0:
	dia = "domingo"
	if soma == 0:
		soma = "domingo"
	elif soma == 1:
		soma = "segunda"
	elif soma == 2:
		soma = "terca"
	elif soma == 3:
		soma = "quarta"
	elif soma == 4:
		soma = "quinta"
	elif soma == 5:
		soma = "sexta"
	elif soma == 6:
		soma = "sabado"
	print ("Hoje eh",dia,"e o dia futuro eh",soma)
	
# Dia 1 - Segunda	
elif dia == 1:
	dia = "segunda"
	if soma == 0:
		soma = "domingo"
	elif soma == 1:
		soma = "segunda"
	elif soma == 2:
		soma = "terca"
	elif soma == 3:
		soma = "quarta"
	elif soma == 4:
		soma = "quinta"
	elif soma == 5:
		soma = "sexta"
	elif soma == 6:
		soma = "sabado"
	print ("Hoje eh",dia,"e o dia futuro eh",soma)
	
# Dia 2 - Terca
elif dia == 2:
	dia = "terca"
	if soma == 0:
		soma = "domingo"
	elif soma == 1:
		soma = "segunda"
	elif soma == 2:
		soma = "terca"
	elif soma == 3:
		soma = "quarta"
	elif soma == 4:
		soma = "quinta"
	elif soma == 5:
		soma = "sexta"
	elif soma == 6:
		soma = "sabado"
	print ("Hoje eh",dia,"e o dia futuro eh",soma)
	
# Dia 3 - Quarta
elif dia == 3:
	dia = "quarta"
	if soma == 0:
		soma = "domingo"
	elif soma == 1:
		soma = "segunda"
	elif soma == 2:
		soma = "terca"
	elif soma == 3:
		soma = "quarta"
	elif soma == 4:
		soma = "quinta"
	elif soma == 5:
		soma = "sexta"
	elif soma == 6:
		soma = "sabado"
	print ("Hoje eh",dia,"e o dia futuro eh",soma)
	
# Dia 4 - Quinta	
elif dia == 4:
	dia = "quinta"
	if soma == 0:
		soma = "domingo"
	elif soma == 1:
		soma = "segunda"
	elif soma == 2:
		soma = "terca"
	elif soma == 3:
		soma = "quarta"
	elif soma == 4:
		soma = "quinta"
	elif soma == 5:
		soma = "sexta"
	elif soma == 6:
		soma = "sabado"
	print ("Hoje eh",dia,"e o dia futuro eh",soma)
	
# Dia 5 - Sexta	
elif dia == 5:
	dia = "sexta"
	if soma == 0:
		soma = "domingo"
	elif soma == 1:
		soma = "segunda"
	elif soma == 2:
		soma = "terca"
	elif soma == 3:
		soma = "quarta"
	elif soma == 4:
		soma = "quinta"
	elif soma == 5:
		soma = "sexta"
	elif soma == 6:
		soma = "sabado"
	print ("Hoje eh",dia,"e o dia futuro eh",soma)
	
# Dia 6 - Sábado	
elif dia == 6:
	dia = "sabado"
	if soma == 0:
		soma = "domingo"
	elif soma == 1:
		soma = "segunda"
	elif soma == 2:
		soma = "terca"
	elif soma == 3:
		soma = "quarta"
	elif soma == 4:
		soma = "quinta"
	elif soma == 5:
		soma = "sexta"
	elif soma == 6:
		soma = "sabado"
	print ("Hoje eh",dia,"e o dia futuro eh",soma)
	
else:
	print ("A entrada",dia,"eh invalida")