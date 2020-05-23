anos = 0
qti=int(input("Quantidade inicial de Tambaquis: "))
pc=float(input("Percentual de crescimento da quantidade de Tambaquis: "))
qtr=int(input("Quantidade de Tambaquis retirados para venda: "))

while (0 < qti < 12000):
	acr=qti*pc/100
	qti = qti + acr
	qti = qti - qtr
	anos = anos + 1
if (qti <= 0):
	print("EXTINCAO")
	print(anos)
else:
	print("LIMITE")
	print(anos)
