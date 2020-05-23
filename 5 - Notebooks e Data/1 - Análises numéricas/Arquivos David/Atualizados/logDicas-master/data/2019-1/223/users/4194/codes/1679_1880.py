var1 = int(input("Digite um numero de 1-12: "))
ja = "janeiro"
fe = "fevereiro"
mr = "marco"
ab = "abril"
ma = "maio"
ju = "junho"
jl = "julho"
ag = "agosto"
se = "setembro"
ou = "outubro"
no = "novembro"
de = "dezembro"

if(1 <= var1 <= 12):
	if(var1==1):
		print(ja)
	elif(var1==2):
		print(fe)
	elif(var1==3):
		print(mr)
	elif(var1==4):
		print(ab)
	elif(var1==5):
		print(ma)
	elif(var1==6):
		print(ju)
	elif(var1==7):
		print(jl)
	elif(var1==8):
		print(ag)
	elif(var1==9):
		print(se)
	elif(var1==10):
		print(ou)
	elif(var1==11):
		print(no)
	elif(var1==12):
		print(de)
else:
	print("numero de mes invalido")