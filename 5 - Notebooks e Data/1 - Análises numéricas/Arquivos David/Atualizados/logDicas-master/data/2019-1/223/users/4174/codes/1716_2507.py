qi = int(input("Quantidade inicial:"))
pc = int(input("Percentual de crescimento:"))

meses = 0
while (0 < qi < 8000):
	qprv = int(input("qpr:"))
	qi = qi + (qi * ( pc/100))
	qi = qi - qprv
	meses = meses + 1
	if(qi <= 0):
		print("ZERO")
	elif (qi >= 8000):
		print("MAXIMO")
print(meses)		