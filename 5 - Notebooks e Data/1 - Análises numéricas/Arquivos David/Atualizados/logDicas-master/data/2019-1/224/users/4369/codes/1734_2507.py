qi = int(input("Quantidade inicial de peixes: "))
pc = float(input("Percentual de crescimento: "))
qm = 8000
pc = pc/100
pt = qi
meses = 0
while pt>=0 and pt<=qm:
	ra = int(input("Retirada de peixes: "))
	pt = (pt + (pt * pc)) -ra
	meses = meses + 1
if pt >= qm:
	print("MAXIMO")
	print(meses)
if pt <= 0:
	print("ZERO")
	print(meses)