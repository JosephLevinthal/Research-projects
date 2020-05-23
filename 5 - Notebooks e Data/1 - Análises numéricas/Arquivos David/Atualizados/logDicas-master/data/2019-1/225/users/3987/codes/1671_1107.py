# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
X = int(input("dia de hoje e: 0/1/2/3/4/5/6" ))
Y = int(input("dias futuros:"))

if(X < 0) or (X > 6):
	s = 7
elif((X + Y) < 7):
	s = X + Y
else:
	s = ((X + Y)%7)
	
if(s == 0):
	e = "domingo"
elif(s == 1):
	e = "segunda"
elif(s == 2):
	e = "terca"
elif(s == 3):
	e = "quarta"
elif(s == 4):
	e = "quinta"
elif(s == 5):
	e = "sexta"
elif(s == 6):
	e = "sabado"
else:
	e = "inexistente"
	
if(X == 0):
	dia = "domingo"
elif(X == 1):
	dia = "segunda"
elif(X == 2):
	dia = "terca"
elif(X == 3):
	dia = "quarta"
elif(X == 4):
	dia = "quinta"
elif(X == 5):
	dia = "sexta"
else:
	dia = "sabado"
	
if(X < 0) or (X > 6):
	print("A entrada", X, "eh invalida")
else:
	print("Hoje eh", dia, "e o dia futuro eh", e)
