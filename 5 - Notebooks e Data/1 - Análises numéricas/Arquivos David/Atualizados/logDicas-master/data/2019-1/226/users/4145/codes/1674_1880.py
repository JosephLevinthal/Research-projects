# Ao testar sua solução, não se limite ao caso de exemplo.
m = int(input("mes do ano: "))
if(1<=m<=12):
	if(m==1):
		m="janeiro"
	elif(m==2):
		m="fevereiro"
	elif(m==3):
		m="marco"
	elif(m==4):
		m="abril"
	elif(m==5):
		m="maio"
	elif(m==6):
		m="junho"
	elif(m==7):
		m="julho"
	elif(m==8):
		m="agosto"
	elif(m==9):
		m="setembro"
	elif(m==10):
		m="outubro"
	elif(m==11):
		m="novembro"
	elif(m==12):
		m="dezembro"
	print(m)	
else:		
	print("numero de mes invalido")