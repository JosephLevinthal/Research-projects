# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
hoje = int(input("Entre com o numero do dia de hoje: "))
futuro = int(input("Entre como  numero de dias apos hoje: " ))
diafuturo = int()

domingo =  "domingo"
segunda = "segunda"
terca = "terca"
quarta = "quarta"
quinta = "quinta"
sexta = "sexta"
sabado = "sabado"


if hoje >= 0 and hoje <= 6:
	print("Hoje eh ", end="")
	if hoje == 0:
		 print(domingo, end="")
	elif hoje == 1:
		 print(segunda, end="")
	elif hoje == 2:
		 print(terca, end="")
	elif hoje == 3:
		 print(quarta, end="")
	elif hoje == 4:
		 print(quinta, end="")
	elif hoje == 5:
		 print(sexta, end="")
	elif hoje == 6:
		 print(sabado, end="")

	if futuro > 7:
		 diafuturo = (futuro + hoje) % 7
	else:
		 diafuturo = futuro

	print(" e o dia futuro eh ", end="")

	if diafuturo == 0:
		 print(domingo, end="")
	elif diafuturo == 1:
		 print(segunda, end="" )
	elif diafuturo == 2:
		 print(terca, end="")
	elif diafuturo == 3:
		 print(quarta, end="")
	elif diafuturo == 4:
		print(quinta, end="")
	elif diafuturo == 5:
		 print(sexta, end="")
	elif diafuturo == 6:
		 print(sabado, end="")
else:
	print("A entrada", hoje, "eh invalida")