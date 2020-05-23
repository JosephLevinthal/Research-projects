i = int(input("Quantidade inicial: "))
pi = float(input("Percentual de crescimento: "))

qua = i
meses = 0

while (qua > 0) and (qua < 8000):
	q = int(input("Quantidade retirada: "))
	qua = qua + qua*pi/100 - q
	meses = meses + 1

if (qua < 0):
	print("ZERO")
elif (qua >= 8000):
	print("MAXIMO")
	
print(meses)