# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = int(input("numero do dia de hj: "))
y = int(input("numero de dias apos hj: "))

df = (x + y)%7
if(x==0 or x==1 or x==2 or x==3 or x==4 or x==5 or x==6):
	if(x == 0):
		x="domingo"
		
		if(df==0):
			df="domingo"
		elif(df==1):	
			df="segunda"
		elif(df==2):
			df="terca"
		elif(df==3):
			df="quarta"
		elif(df==4):
			df="quinta"
		elif(df==5):
			df="sexta"
		elif(df==6):
			df="sabado"
			
	elif(x==1):
		x="segunda"
		if(df==0):
			df="domingo"
		elif(df==1):	
			df="segunda"
		elif(df==2):
			df="terca"
		elif(df==3):
			df="quarta"
		elif(df==4):
			df="quinta"
		elif(df==5):
			df="sexta"
		elif(df==6):
			df="sabado"
	elif(x==2):	
		x="terca"
		if(df==0):
			df="domingo"
		elif(df==1):	
			df="segunda"
		elif(df==2):
			df="terca"
		elif(df==3):
			df="quarta"
		elif(df==4):
			df="quinta"
		elif(df==5):
			df="sexta"
		elif(df==6):
			df="sabado"
	elif(x==3):
		x="quarta"
		if(df==0):
			df="domingo"
		elif(df==1):	
			df="segunda"
		elif(df==2):
			df="terca"
		elif(df==3):
			df="quarta"
		elif(df==4):
			df="quinta"
		elif(df==5):
			df="sexta"
		elif(df==6):
			df="sabado"
	elif(x==4):
		x="quinta"
		if(df==0):
			df="domingo"
		elif(df==1):	
			df="segunda"
		elif(df==2):
			df="terca"
		elif(df==3):
			df="quarta"
		elif(df==4):
			df="quinta"
		elif(df==5):
			df="sexta"
		elif(df==6):
			df="sabado"
	elif(x==5):
		x="sexta"
		if(df==0):
			df="domingo"
		elif(df==1):	
			df="segunda"
		elif(df==2):
			df="terca"
		elif(df==3):
			df="quarta"
		elif(df==4):
			df="quinta"
		elif(df==5):
			df="sexta"
		elif(df==6):
			df="sabado"
	elif(x==6):
		x="sabado"
		if(df==0):
			df="domingo"
		elif(df==1):	
			df="segunda"
		elif(df==2):
			df="terca"
		elif(df==3):
			df="quarta"
		elif(df==4):
			df="quinta"
		elif(df==5):
			df="sexta"
		elif(df==6):
			df="sabado"
			
	print("Hoje eh ",x," e o dia futuro eh",df)	
else:
	print("A entrada ",x," eh invalida")