# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = int(input("Entre com o numero do dia de hoje: (0/1/2/3/4/5/6) "))
y = int(input("Entre com o numero de dias apos hoje: "))
z = x%y
if(0 <= z) and (z <= 6):
	print("Hoje eh", x ,"e o dia futuro eh", y)
	if(x==1):
		print("segunda")
	elif(x==2):
		print("terca")
	elif(x==3): 
		print("quarta")
	elif(x==4):
		print("Hoje eh", x ,"e o dia futuro eh", y)
	elif(x==5):
		print("sexta")
	elif(x==6):
		print("sabado")
	else:
		print("A entrada", x ,"eh invalida")
else: 
	print("A entrada", x ,"eh invalida")