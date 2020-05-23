qp = int(input("quantidade de peixes: "))
pc = int(input("percentual de cescimento: "))
qr = int(input("quantidades de pirarucus retirados: "))

cap = 8000

mes = 0 #variavel contadora 

while (qp >0) and (qp<cap):
	qp = qp + (qp * (pc/100)) - qr # acumula o n. de peixes
	mes = mes + 1 # atuailiza n. de peixes
	
	if (qp >= cap):
		print("MAXIMO")
	elif (qp <= 0):
		print("ZERO")
	else:
		qr = int(input("no. mensal de peixes retirados: "))
print(mes)