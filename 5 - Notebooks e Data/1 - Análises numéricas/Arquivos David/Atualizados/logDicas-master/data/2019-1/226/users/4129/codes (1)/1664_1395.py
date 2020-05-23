vendeu = float(input("Valor de vendas:"))
execed = vendeu-1000
dez = (1000*0.05)+(execed*0.1)
if(vendeu<=1000):
	cinco = vendeu*0.05
	print(round(cinco, 2))
if(vendeu>1000):
	print(round(dez, 2))