# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = int(input("n:"))
j = int(input("Quantos dias? "))
if((x>=0)and(x<=6)):
	d1 = (x+j)%7
	if(x==0):
		y= "domingo"
	elif(x==1):
		y= "segunda"
	elif(x==2):
		y= "terca"
	elif(x==3):
		y= "quarta"
	elif(x==4):
		y= "quinta"
	elif(x==5):
		y= "sexta"
	else:
		y= "sabado"
	if(d1==0):
		z= "domingo"
	elif(d1==1):
		z= "segunda"
	elif(d1==2):
		z= "terca"
	elif(d1==3):
		z= "quarta"
	elif(d1==4):
		z= "quinta"
	elif(d1==5):
		z= "sexta"
	else:
		z= "sabado"
	print("Hoje eh",y,"e o dia futuro eh",z)
else:
	print("A entrada",x,"eh invalida")
   