# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a = int(input("dia de hoje: "))
b = int(input("numero de dias apos hoje: "))
#c = int(input("numero: "))
x = "Hoje eh"
y = " e o dia futuro eh "
c = (a+b)%7
if(a==0):
	a = "domingo"
	if(c==0):
		c = "domingo"
	elif(c==1):
		c = "segunda"
	elif(c==2):