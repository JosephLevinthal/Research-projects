# Ao testar sua solução, não se limite ao caso de exemplo.
m = int(input("Digite um numero que equivale a um mes(1~12?:)"))
if((1<=m)and(m<=12)):
	if(m==1):
		print("janeiro")
	elif(m==2):
		print("fevereiro")
	elif(m==3):
		print("marco")
	elif(m==4):
		print("abril")
	elif(m==5):
		print("maio")
	elif(m==6):
		print("junho")
	elif(m==7):
		print("julho")
	elif(m==8):
		print("agosto")
	elif(m==9):
		print("setembro")
	elif(m==10):
		print("outubro")
	elif(m==11):
		print("novembro")
	elif(m==12):
		print("dezembro")
	else:
		print("numero de mes invalido")
else:
	print("numero de mes invalido")
		
	