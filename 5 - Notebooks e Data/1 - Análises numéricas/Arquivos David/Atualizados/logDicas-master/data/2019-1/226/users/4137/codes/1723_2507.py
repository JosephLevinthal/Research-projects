qti = int(input("quantidade inicial:"))
pc = int(input("Percentual de crescimento:"))/100

mes = 0
soma = 0

while(qti> 0 and qti < 8000):
	venda = int(input("Quantidade de venda:"))
	qti = qti*pc + qti
	qti = qti - venda
	mes = mes + 1
if(qti <= 0):
	print("ZERO")
if(qti > 8000):
	print("MAXIMO")
print(mes)