dia = int(input("dia de hoje: "))
diafu = int(input("dias futuros: "))

futuro = (dia+diafu)%7
if(dia>=0)and(dia<=6):
	if(diafu>0):
		if(dia==0):
			x="domingo"
		elif(dia==1):
			x="segunda"
		elif(dia==2):
			x="terca"
		elif(dia==3):
			x="quarta"
		elif(dia==4):
			x="quinta"
		elif(dia==5):
			x="sexta"
		elif(dia==6):
			x="sabado"
		if(futuro==0):
			y="domingo"
		elif(futuro==1):
			y="segunda"
		elif(futuro==2):
			y="terca"
		elif(futuro==3):
			y="quarta"
		elif(futuro==4):
			y="quinta"
		elif(futuro==5):
			y="sexta"
		elif(futuro==6):
			y="sabado"
		print("Hoje eh", x, "e o dia futuro eh", y)
	else:
		print("A entrada", diafu, "eh invalida")
else:
	print("A entrada", dia, "eh invalida")
	
		