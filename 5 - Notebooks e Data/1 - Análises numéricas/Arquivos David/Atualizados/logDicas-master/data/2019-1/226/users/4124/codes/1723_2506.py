qp = int(input("Quantidade inicial de peixes: "))
pc = float(input("Percentual de crescimento anual: "))/100
qr = int(input("Quantidade retirada de peixes: "))
a = 0
while(qp > 0 and qp < 12000):

	qp = qp + (qp * pc) - qr
	a = a + 1
if(qp >= 12000):
	print("LIMITE")
elif(qp <= 0):
	print("EXTINCAO")
print(a)