qic = int(input("copias:"))
qil = int(input("leucocitos:"))
perc1 = int(input("p do virus:"))/100
perc2 = int(input("p do leucocito:"))/100

dias = 0

while(qic > qil/2 ):
	qic = qic + (qic * perc1)
	qil = qil + (qil * perc2)
	dias = dias + 1
print(dias)	