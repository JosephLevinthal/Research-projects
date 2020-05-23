genero = input("Mulher? : ")
preco = float(input("valor ingresso: "))
qt = int(input("quantidade ingressos: "))

if genero == "S":
	preco2 = preco - preco * (1 / 5)
	preco3 = preco2 * qt
	print(round(preco3,2))
else:
	print(round(preco*qt,2))