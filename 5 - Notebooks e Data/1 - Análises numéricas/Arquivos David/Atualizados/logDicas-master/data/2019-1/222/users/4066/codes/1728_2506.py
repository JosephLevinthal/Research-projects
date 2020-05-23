i = int(input("Quantidade inicial: "))
pi = float(input("Percentual de crescimento: "))
q = int(input("Quantidade retirada: "))

t = 0
qua = i
anos = 0
while (qua > 0) and (qua <= 12000):
	qua = qua + qua*pi/100 - q
	anos = anos + 1
if (qua < 0):
	print("EXTINCAO")
elif(qua >= 12000):
	print("LIMITE")

print(anos)