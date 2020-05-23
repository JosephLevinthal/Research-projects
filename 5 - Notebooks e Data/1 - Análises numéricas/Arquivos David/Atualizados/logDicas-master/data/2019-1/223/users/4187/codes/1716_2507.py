QIP = int(input("quantidade de inicial de piraruucus:"))
PCM = int(input("percentual de crescimento mensal no tamque de pirarucus:"))/100

meses = 0
while(QIP > 0 and QIP < 8000):
	PirVenMes = int(input("Quantidade de pirarucus retirado para venda por mes:"))
	QIP = QIP + (QIP * PCM )
	QIP = QIP - PirVenMes
	meses = meses + 1
	if(QIP <= 0):
		print("zero".upper())
	elif(QIP >= 8000):
		print("maximo".upper())
print(meses)