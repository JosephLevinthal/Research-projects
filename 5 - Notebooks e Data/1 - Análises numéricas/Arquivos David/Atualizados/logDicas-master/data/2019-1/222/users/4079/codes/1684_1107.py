# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
h=int(input("hoje:"))
if(h>=0 and h<=6):
	f=int(input("dia futuro:"))
	if(h==0):
		x="domingo"
		if((h+f)%7==0):
			y="domingo"
		elif((h+f)%7==1):
			y="segunda"
		elif((h+f)%7==2):
			y="terca"
		elif((h+f)%7==3):
			y="quarta"
		elif((h+f)%7==4):
			y="quinta"
		elif((h+f)%7==5):
			y="sexta"
		elif((h+f)%7==6):
			y="sabado"
		
	elif(h==1):
		x="segunda"
		if((h+f)%7==0):
			y="domingo"
		elif((h+f)%7==1):
			y="segunda"
		elif((h+f)%7==2):
			y="terca"
		elif((h+f)%7==3):
			y="quarta"
		elif((h+f)%7==4):
			y="quinta"
		elif((h+f)%7==5):
			y="sexta"
		elif((h+f)%7==6):
			y="sabado"
		
	elif(h==2):
		x="terca"
		if((h+f)%7==0):
			y="domingo"
		elif((h+f)%7==1):
			y="segunda"
		elif((h+f)%7==2):
			y="terca"
		elif((h+f)%7==3):
			y="quarta"
		elif((h+f)%7==4):
			y="quinta"
		elif((h+f)%7==5):
			y="sexta"
		elif((h+f)%7==6):
			y="sabado"

	elif(h==3):
		x="quarta"
		if((h+f)%7==0):
			y="domingo"
		elif((h+f)%7==1):
			y="segunda"
		elif((h+f)%7==2):
			y="terca"
		elif((h+f)%7==3):
			y="quarta"
		elif((h+f)%7==4):
			y="quinta"
		elif((h+f)%7==5):
			y="sexta"
		elif((h+f)%7==6):
			y="sabado"

	elif(h==4):
		x="quinta"
		if((h+f)%7==0):
			y="domingo"
		elif((h+f)%7==1):
			y="segunda"
		elif((h+f)%7==2):
			y="terca"
		elif((h+f)%7==3):
			y="quarta"
		elif((h+f)%7==4):
			y="quinta"
		elif((h+f)%7==5):
			y="sexta"
		elif((h+f)%7==6):
			y="sabado"
			
	elif(h==5):
		x="sexta"
		if((h+f)%7==0):
			y="domingo"
		elif((h+f)%7==1):
			y="segunda"
		elif((h+f)%7==2):
			y="terca"
		elif((h+f)%7==3):
			y="quarta"
		elif((h+f)%7==4):
			y="quinta"
		elif((h+f)%7==5):
			y="sexta"
		elif((h+f)%7==6):
			y="sabado"
	
	elif(h==6):
		x="sabado"
		if((h+f)%7==0):
			y="domingo"
		elif((h+f)%7==1):
			y="segunda"
		elif((h+f)%7==2):
			y="terca"
		elif((h+f)%7==3):
			y="quarta"
		elif((h+f)%7==4):
			y="quinta"
		elif((h+f)%7==5):
			y="sexta"
		elif((h+f)%7==6):
			y="sabado"
			
	print("Hoje eh",x," e o dia futuro eh",y)
else:
	print("A entrada",h,"eh invalida")