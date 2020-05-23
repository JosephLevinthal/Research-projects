

QItam = int(input("Quantidade inicial de tambaquis no tanque:"))
cresTam = int(input("Percentual de crescimento anual da quantidade de tambaquis no tamque: "))/100
QTamVen = int(input("Quantidade de tambaquis retirados todos os anos para venda: "))

anos = 0 
QT = QItam
while(QT  > 0 and QT < 12000):
	QT = QT + (QT * cresTam)
	QT = QT - QTamVen
	anos = anos + 1
	if(QT <= 0):
		print("extincao".upper())
	elif(QT >= 12000):
		print("limite".upper())
print(anos)