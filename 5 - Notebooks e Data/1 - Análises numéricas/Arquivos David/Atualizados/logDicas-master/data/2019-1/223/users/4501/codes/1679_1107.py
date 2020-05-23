# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a=int(input("dia semana : "))
if(a<0 or a>6):
	print("A entrada",a,"eh invalida")
else: 
	fut=int(input("Dias futuro: "))
	if(a+fut>6):
		x=(a+fut)%7
	else:
		x=a+fut
	if(x==0):
		x="domingo"
	elif(x==1):
		x="segunda"
	elif(x==2):
		x="terca"
	elif(x==3 ):
		x="quarta"
	elif(x==4):
		x="quinta"
	elif(x==5):
		x="sexta"
	elif(x==6):
		x="sabado"
		
	
	if(a==0):
		a="domingo"	
	elif(a==1):
		a="segunda"
	elif(a==2):
		a="terca"
	elif(a==3 ):
		a="quarta"
	elif(a==4):
		a="quinta"
	elif(a==5):
		a="sexta"
	elif(a==6):
		a="sabado"
		
	print("Hoje eh",a,"e o dia futuro eh",x)
		
