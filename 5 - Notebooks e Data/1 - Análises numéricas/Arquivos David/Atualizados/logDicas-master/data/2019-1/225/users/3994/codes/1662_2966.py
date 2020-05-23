opcao = input("S/N?: ")
preco = float(input(" Digite o preco: "))
q = int(input(" Digite quantidade: "))
d = 20/100
if(opcao == "S"):
	a = (preco - ((d) * preco))
	valor = a * q
	print(round(valor,2))
else:
	valor = preco * q
	print(round(valor,2))