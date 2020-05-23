# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
n = int(input("Insira o dia da semana:"))
n1 = int(input("Insira numero do futuro:"))

df = n+n1

if(n < 0 or n > 7):
	print("A entrada", n, "eh invalida")
else:
	
	if(df>6):
		e = df%7
	else:
		e = df

	if(e == 1):
		e =("segunda")
	elif(e == 2):
		e =("terca")
	elif(e == 3):
		e =("quarta")
	elif(e == 4):
		e =("quinta")
	elif(e == 5):
		e =("sexta")
	elif(e == 6):
		e =("sabado")	
	elif(e == 0):
		e =("domingo")

	if(n == 1):
		x =("segunda")
	elif(n == 2):
		x =("terca")
	elif(n == 3):
		x =("quarta")
	elif(n == 4):
		x =("quinta")
	elif(n == 5):
		x =("sexta")
	elif(n == 6):
		x =("sabado")	
	elif(n == 0):
		x =("domingo")

	print("Hoje eh", x ,"e o dia futuro eh" , e)	
