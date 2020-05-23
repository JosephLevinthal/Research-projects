pe = float(input("Digite o peso da encomenda: "))
if(pe < 5000):
	f = pe * 0.05
	print(round(f, 2))
else:
	f = (pe * 0.04) + 60
	print(round(f, 2))
