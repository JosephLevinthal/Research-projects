# Ao testar sua solução, não se limite ao caso de exemplo.
a = int(input("numero do mes:"))

if(a>0)and(a<13):
	if(a==1):
		print("janeiro")
	elif(a==2):
		print("fevereiro")
	elif(a==3):
		print("marco")
	elif(a==4):
		print("abril")
	elif(a==5):
		print("maio")
	elif(a==6):
		print("junho")
	elif(a==7):
		print("julho")
	elif(a==8):
		print("agosto")
	elif(a==9):
		print("setembro")
	elif(a==10):
		print("outubro")
	elif(a==11):
		print("novembro")
	elif(a==12):
		print("dezembro")
else:
	print("numero de mes invalido")