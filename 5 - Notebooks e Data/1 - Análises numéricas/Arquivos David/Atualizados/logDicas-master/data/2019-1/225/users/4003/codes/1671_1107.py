# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

dia_semana = int(input("dia: (0 a 6) "))
dia_fut = int(input("Entre com o numero de dias apos hoje: "))

if (dia_semana < 0) or (dia_semana > 6):
	sol = 7
elif ((dia_semana+dia_fut) < 7):
	sol = dia_semana + dia_fut
else:
	sol = ((dia_semana+dia_fut) % 7)
	
if sol == 0:
	esp = "domingo"
elif sol == 1:
	esp = "segunda"
elif sol == 2:
	esp = "terça"
elif sol == 3:
	esp = "quarta"
elif sol == 4:
	esp = "quinta"
elif sol == 5:
	esp = "sexta"
elif sol == 6:
	esp = "sabado"
else:
	esp = "inexistente"
	
if dia_semana == 0: 
	dia = "domingo"
elif dia_semana == 1:
	dia = "segunda"
elif dia_semana == 2:
	dia = "terça"
elif dia_semana == 3:
	dia = "quarta"
elif dia_semana == 4:
	dia = "quinta"
elif dia_semana == 5:
	dia = "sexta"
else:
	dia = "sabado"	
	
if (dia_semana <0) or (dia_semana > 6):
	print("A entrada", dia_semana, "eh invalida")
else:
	print("Hoje eh", dia, "e o dia futuro eh", esp)