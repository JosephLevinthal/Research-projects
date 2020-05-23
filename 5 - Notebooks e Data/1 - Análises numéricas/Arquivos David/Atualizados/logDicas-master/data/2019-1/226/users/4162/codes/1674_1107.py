d= int(input("Entre com o numero do dia de hoje: "))
df= int(input("Entre com o numero de dias apos hoje: "))
if ((d+df)%7==0):
	df=("domingo")
elif((d+df)%7==1):
	df=("segunda")
elif ((d+df)%7==2):
	df=("terca")
elif((d+df)%7==3):
	df=("quarta")
elif((d+df)%7==4):
	df=("quinta")
elif((d+df)%7==5):
	df=("sexta")
elif((d+df)%7==6):
	df=("sabado")
if (d>=0)and(d<=6):
	if (d==0):
		d=("domingo")
	elif (d==1):
		d=("sugunda")
	elif (d==2):
		d=("terca")
	elif (d==3):
		d=("quarta")
	elif (d==4):
		d=("quinta")
	elif (d==5):
		d=("sexta")
	elif (d==6):
		d=("sabado")
	print("Hoje eh",d,"e o dia futuro eh",df)
else:
	print ("A entrada",d,"eh invalida")
