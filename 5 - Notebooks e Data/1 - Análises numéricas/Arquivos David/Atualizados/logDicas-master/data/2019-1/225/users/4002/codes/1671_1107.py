# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
hoje = float(input("Entre com o numero do dia de hoje: "))
futuro = float(input("Entre com o numero de dias apos hoje: "))
if(hoje == 0):
	dia = "domingo"
elif (hoje == 1):
	dia = "segunda"
elif (hoje == 2):
	dia = "terca"
elif (hoje == 3):
	dia = "quarta"
elif (hoje == 4):
	dia = "quinta"
elif (hoje == 5):
	dia = "sexta"
elif (hoje == 6):
	dia = "sabado"
else:
	print("A entrada hoje eh invalida") 
soma = hoje + futuro	komk
if (soma == 0):
	fut = "domingo"
elif (soma == 1):
	fut = "segunda"
elif (soma == 2):
	fut = "terca"
elif (soma == 3):
	fut = "quarta"
elif (soma == 4):
	fut = "quinta"
elif (soma == 5):
	fut = "sexta"
elif (soma == 6):
	fut = "sabado"

print("hoje eh", dia, "e o dia do futuro eh", fut)