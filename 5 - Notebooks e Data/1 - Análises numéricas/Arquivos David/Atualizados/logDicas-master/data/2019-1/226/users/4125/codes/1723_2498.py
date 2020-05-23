nA = int(input("numero de habitantes na cidade a: "))
nB = int(input("numero de habitantes na cidade b: "))
pA = float(input("digite o percentual de crescimento na cidade a: "))/100
pB = float(input("digite o percentual de crescimento na cidade b: "))/100

anos = 0
while(nA<nB):
	nA = nA + nA*pA
	nB = nB + nB*pB
	anos = anos + 1
print(anos)