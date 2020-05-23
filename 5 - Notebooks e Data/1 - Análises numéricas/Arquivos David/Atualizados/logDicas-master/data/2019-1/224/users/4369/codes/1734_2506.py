qi = int(input("Quantidade inicial de peixes: "))
pc = float(input("Percentual de crescimento: "))
ra = int(input("Retirada de peixes: "))
qm = 12000
pc = pc/100
pt = qi
anos = 0
while pt>=0 and pt<=qm:
	pt = (pt + (pt * pc)) -ra
	anos = anos + 1
if pt >= qm:
	print("LIMITE")
	print(anos)
if pt <= 0:
	print("EXTINCAO")
	print(anos)