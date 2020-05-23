a=int(input())
if(a!=0 and a!=1 and a!=2  and a!=3 and a!=4 and a!=5 and a!=6):
	print("A entrada", a ,"eh invalida")
else:
	b=int(input())
	conta1=(a+b)%7
	if(a==0):
		a="domingo"
	elif (a==1):
		a="segunda"
	elif(a==2):
		a="terca"
	elif (a==3):
		a="quarta"
	elif a==4:
		a="quinta"
	elif a==5:
		a="sexta"
	elif(a==6):
		a="sabado"
	if conta1==0:
		conta="domingo"
	elif conta1==1:
		conta1="segunda"
	elif conta1==2:
		conta1=="terca"
	elif conta1==3:
		conta1="quarta"
	elif conta1==4:
		conta1="quinta"
	elif conta1==5:
		conta1="sexta"
	elif conta1==6:
		conta1="sabado"
	print("Hoje eh", a ,"e o dia futuro eh", conta1)
	
	
		
		

