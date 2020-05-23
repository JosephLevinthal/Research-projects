d = int (input("Qualodia"))
if((d>=0 and d<=6)):
	j = int(input("quantos dias"))
	d1= (d+j)%7
	if(d==0):
		d= "domingo"
	elif(d==1):
		print("segunda")
	elif(d==2):
		d= "terça"
	elif(d==3):
		d= "quarta"	
	elif(d==4):
		d= "quinta"	
	elif(d==5):
		d= "sexta"
	elif(d==6):
		d= "sabado"
	elif(d1==0):
		d1="domingo"
	elif(d1=1):
		d1= "segunda"
	elif(d1==2):
		d1= "terça"
	elif(d1==3):
		d1= "quarta"
	elif(d1==4):
		d1= "quinta"
	elif(d1==5):
		d1= "sexta"
	elif(d1==6):
		d1= "sabado"	
	
	print("Hoje eh",d,"e o dia futuro eh",d1)
else:
	print("A entrada",d,"eh invalida")
		