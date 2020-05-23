arma=input("digite o nome da arma: (cimitarra/katana/sabre)").upper()
des=float(input("digite o valor da destreza: "))
val1=int(input("didite o valor dado 1"))
val2=int(input("digite o valor dado 2: "))
danoci=2*(val1+val2)+(2*des)
danokat=2*(val1+val2)+des
danosa=(val1+val2)+(2*des)


if(arma=="CIMITARRA")or(arma=="KATANA")or(arma=="SABRE"):
	if (val1<=10)and(val1>=1) and(val2<=10)and(val2>=1)and(des>=0):
		if(arma=="CIMITARRA"):
			print(danoci)
		elif(arma=="KATANA"):
			print(danokat)
		elif(arma=="SABRE"):
			print(danosa)
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")
	
		