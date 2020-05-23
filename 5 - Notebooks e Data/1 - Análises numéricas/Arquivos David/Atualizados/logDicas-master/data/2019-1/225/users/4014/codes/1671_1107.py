# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=int(input("numero dia:"))
y=int(input("dias no futuro:"))
if((x<=6) and (x>=0)):
	if(x==0):
		Z="domingo"
	elif(x==1):
		Z="segunda"
	elif(x==2):
		Z="terca"
	elif(x==3):
		Z="quarta"
	elif(x==4):
		Z="quinta"
	elif(x==5):
		Z="sexta"
	else:
		Z="sabado"
		
	if((x + y)%7 ==0):
		A="domingo"
	elif((x+y)%7==1):
		A="segunda"
	elif((x+y)%7==2):
		A="terca"
	elif((x+y)%7==3):
		A="quarta"
	elif((x+y)%7==4):
		A="quinta"
	elif((x+y)%7==5):
		A="sexta"
	else:
		A="sabado"
	print("Hoje eh",Z,"e o dia futuro eh",A)
else:
	print("A entrada",x,"eh invalida")
	