qp = int(input("Qi: "))
pc = int(input("perc: "))
qr = int(input("Quantidade: "))

mes = 0
cap = 8000

while(qp>0) and (qp<cap):
	qp = qp + (qp * pc/100) - qr
	mes = mes + 1
	if(qp >= 0):
		print("MAXIMO")
	elif(qp <= 0):
		print("ZERO")
	else:
		qr = int(input("vai: "))

print(mes)