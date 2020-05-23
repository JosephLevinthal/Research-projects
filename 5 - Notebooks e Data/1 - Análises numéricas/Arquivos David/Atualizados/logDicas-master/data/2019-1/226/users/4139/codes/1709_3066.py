qv = int(input("quantidade inicial de vida:"))
s1 = int(input("valor sorteado 1:"))
s2 = int(input("valor sorteado 2:"))
s3 = int(input("valor sorteado 3:"))

if(s1>0)and(s2>0)and(s3>0)and(s1<=12)and(s2<=12)and(s3<=12)and(qv>0):
	x = qv -(10*s1+10*s2+10*s3)
	if(x<=0):
		print(0)
		print("MORTO")
	elif(x>0):
		print(x)
		print("VIVO")
else:
	print("Entrada invalida")