qi = int(input("quantidade inicial: "))
pc = int(input("percentual de crescimento mensal: "))

meses = 0

while(0 < qi < 8000):
	qprv = int(input("Quantidade para venda mes: "))
	qi = qi + (qi * (pc/100))
	qi = qi - qprv
	meses = meses + 1
	if(qi <= 0):
		print("ZERO")
	elif(qi >= 8000):
		print("MAXIMO")
print(meses)