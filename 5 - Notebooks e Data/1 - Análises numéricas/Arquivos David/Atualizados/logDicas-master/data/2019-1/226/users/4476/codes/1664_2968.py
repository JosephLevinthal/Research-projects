tipo = input("lanche ou salgado? (L/S) ")
qt = int(input("quantidade de lanches ou salgados: "))
qtr = int(input("quantidade de refrigerantes: "))

if (tipo.upper() == "L" ):
	preco = (5.00*qt) + (4.00*qtr)
	print(round(preco, 2))
	
else:
	preco = (3.50*qt) + (4.00*qtr)
	print(round(preco, 2))
