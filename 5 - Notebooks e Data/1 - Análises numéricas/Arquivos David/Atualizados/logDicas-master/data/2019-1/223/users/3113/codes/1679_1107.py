# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

x=int(input("Entre com o numero do dia de hoje:"))
y=int(input("Entre com o numero de dias apos hoje:"))

d=y%7+x

if(x<=6):
	if(x==0):
		s="domingo"
	elif(x==1):
		s="segunda"
	elif(x==2):
		s="terca"
	elif(x==3):
		s="quarta"
	elif(x==4):
		s="quinta"
	elif(x==5):
		s="sexta"
	elif(x==6):	
		s="sabado"
	if(d>6):
		d=d-7	
	if(d==0):
		d="domingo"
	if(d==1):
		d="segunda"
	if(d==2):
		d="terca"
	if(d==3):
		d="quarta"
	if(d==4):
		d="quinta"
	if(d==5):
		d="sexta"
	if(d==6):
		d="sabado"
	print("Hoje eh", s,"e o dia futuro eh", d)
else:
	print("A entrada", x,"eh invalida")


