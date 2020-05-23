# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
dia_hoje = int(input("Entre com o numero do dia de hoje: "))
dia_apos = int(input("Entre com o numero de dias apos hoje: "))
futuro = (dia_hoje + dia_apos) % 7
#numero do dia da semana
if(0<= dia_hoje <7):
	if(dia_hoje == 0):
		dia_hoje = "domingo"
	if(dia_hoje == 1):
		dia_hoje = "segunda"
	if(dia_hoje == 2):
		dia_hoje = "terca"
	if(dia_hoje == 3):
		dia_hoje = "quarta"
	if(dia_hoje == 4):
		dia_hoje = "quinta"
	if(dia_hoje == 5):
		dia_hoje = "sexta"
	if(dia_hoje == 6):
		dia_hoje = "sabado"
#futuro que é a soma do dia da semana + os dias apos pela divisao de resto 7 que dá valores de 0 a 6
	if(futuro == 0):
		futuro = "domingo"
		print("Hoje eh",dia_hoje,"e o dia futuro eh",futuro)
	if(futuro == 1):
		futuro = "segunda"
		print("Hoje eh",dia_hoje,"e o dia futuro eh",futuro)
	if(futuro == 2):
		futuro = "terca"
		print("Hoje eh",dia_hoje,"e o dia futuro eh",futuro)
	if(futuro == 3):
		futuro = "quarta"
		print("Hoje eh",dia_hoje,"e o dia futuro eh",futuro)
	if(futuro == 4):
		futuro = "quinta"
		print("Hoje eh",dia_hoje,"e o dia futuro eh",futuro)
	if(futuro == 5):
		futuro = "sexta"
		print("Hoje eh",dia_hoje,"e o dia futuro eh",futuro)
	if(futuro == 6):
		futuro = "sabado"
		print("Hoje eh",dia_hoje,"e o dia futuro eh",futuro)
else:
	print("A entrada",dia_hoje,"eh invalida")


	
	
	