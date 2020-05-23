# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
n = int(input("numero: "))
dia = int(input("futuro: "))
if n>=0 and n<=6:
	var= (n+dia)%7
	if n == 0:
		tex_n = "domingo"
	elif n == 1:
		tex_n = "segunda"
	elif n == 2:
		tex_n = "terca"
	elif n == 3:
		tex_n = "quarta"
	elif n==4:
		tex_n = "quinta"
	elif n==5:
		tex_n = "sexta"
	else:
		tex_n = "sabado"
	if var == 0:
		tex = "domingo"
	elif var == 1:
		tex = "segunda"
	elif var == 2:
		tex = "terca"
	elif var == 3:
		tex = "quarta"
	elif var ==5:
		tex = "quinta"
	else:
		tex = "sexta"
	print("Hoje eh",tex_n, "e o dia futuro eh",tex)
else:
	print("A entrada",n,"eh invalida")