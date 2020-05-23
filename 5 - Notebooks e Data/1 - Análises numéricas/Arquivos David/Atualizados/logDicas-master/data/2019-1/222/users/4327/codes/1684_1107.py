# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

dia = int(input("Numero do dia de hoje: "))
dp = int(input("Numero de dias apos hoje: "))

# Baseando-se que quando passam 7 dias, estaremos no mesmo dia (da semana).
# Por exemplo, hoje é sábado, se se passarem 7 dias, será sabado de novo.
# Logo os dias a mais serão o resto da divisão por 7
resto = dp % 7
# O dia futuro será o dia que estamos na semama mais os dias que se passaram,
# ou o resto da divisão por 7, melhor dizendo.
df = (resto + dia)%7

# Relacionando o numero do dia com o dia da semana(nome)
if (dia == 0):
	hoje = 'domingo'
elif (dia == 1):
	hoje = 'segunda'
elif (dia == 2):
	hoje = 'terca'
elif (dia == 3):
	hoje = 'quarta'
elif (dia == 4):
	hoje = 'quinta'
elif (dia == 5):
	hoje = 'sexta'
elif (dia == 6):
	hoje = 'sabado'
else:
	# Verificando se a entrada "DIA" é valida.
	hoje = 'invalido'
	
# Se a entrada for valida, então continuamos o calculo do dia seguinte.
if (hoje!='invalido'):
	# Relacionando o numero do dia futuro com o dia da semana(nome).
	if(df == 0):
		diaf = 'domingo'
	elif (df == 1):
		diaf = 'segunda'
	elif (df == 2):
		diaf = 'terca'
	elif (df == 3):
		diaf = 'quarta'
	elif (df == 4):
		diaf = 'quinta'
	elif (df == 5):
		diaf = 'sexta'
	elif (df == 6):
		diaf = 'sabado'
	print("Hoje eh {} e o dia futuro eh {}".format(hoje,diaf))
else:
	print("A entrada {} eh invalida".format(dia))
