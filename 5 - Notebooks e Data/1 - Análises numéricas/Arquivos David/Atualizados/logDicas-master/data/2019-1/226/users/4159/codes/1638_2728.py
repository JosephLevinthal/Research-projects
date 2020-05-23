p = float(input("km: "))
carro = input(" A ou B ").upper()
if(carro=="A"):
	print(round(p/8, 2))
else:
	print(round(p/12, 2))