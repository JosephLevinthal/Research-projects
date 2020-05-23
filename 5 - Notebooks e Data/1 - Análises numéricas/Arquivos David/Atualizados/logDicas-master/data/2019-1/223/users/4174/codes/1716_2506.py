QI = int(input("Quantidade inicial:"))
PC = float(input("Percentual de crescimento:"))
QTR = int(input("Quantidade:"))

anos = 0
QT = QI
while(0 < QT < 12000):
	QT = QT + (QT * PC/100)
	QT = QT - QTR
	anos = anos + 1
	if (QT <= 0):
		print("EXTINCAO")
	elif(QT >= 12000):
		print("LIMITE")
print(anos)