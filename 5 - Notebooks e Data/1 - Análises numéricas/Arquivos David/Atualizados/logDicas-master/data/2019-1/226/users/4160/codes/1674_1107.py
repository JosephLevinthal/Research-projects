# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
d = int(input("Entre com o numero do dia de hoje: "))
f = int(input("Entre com o numero de dias apos hoje: "))

r = (d+f) % 7

if (d>=7 or d <=0):
	print ("A entrada", d,"eh invalida" )
else:
	if (d==0):
		x = "domingo"
	if (d==1):
		x ="segunda"
	if (d==2):
		x ="terca"
	if (d==3):
		x ="quarta"
	if (d==4):
		x ="quinta"
	if (d==5):
		x ="sexta"
	if (d==6):
		x ="sabado"
	if (r==0):
		y ="domingo"
	if (r==1):
		y ="segunda"
	if (r==2):
		y ="terca"
	if (r==3):
		y ="quarta"
	if (r==4):
		y ="quinta"
	if (r==5):
		y ="sexta"
	if (r==6):
		y ="sabado"
	
	print("Hoje eh", x, "e o dia futuro eh",y)	
		

		
		
		
		
		
		
		
		
		

