# Ao testar sua solução, não se limite ao caso de exemplo.
m= int(input("Insira o mes:"))
x1="janeiro"
x2="fevereiro"
x3="marco"
x4="abril"
x5="maio"
x6="junho"
x7="julho"
x8="agosto"
x9="setembro"
x10="outubro"
x11="novembro"
x12="dezembro"
if(1<=m and m<=12):
	if(m==1):
		print(x1.lower())
	elif(m==2):
		print(x2.lower())
	elif(m==3):
		print(x3.lower())
	elif(m==4):
		print(x4.lower())
	elif(m==5):
		print(x5.lower())
	elif(m==6):
		print(x6.lower())
	elif(m==7):
		print(x7.lower())
	elif(m==8):
		print(x8.lower())
	elif(m==9):
		print(x9.lower())
	elif(m==10):
		print(x10.lower())
	elif(m==11):
		print(x11.lower())
	elif(m==12):
		print(x12.lower())
else:
	print("numero de mes invalido")