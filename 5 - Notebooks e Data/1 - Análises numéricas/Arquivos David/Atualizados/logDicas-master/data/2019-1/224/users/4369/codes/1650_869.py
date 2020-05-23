valor = float(input("Digite valor: "))
if(valor >= 200):
	desconto = (valor - valor*5/100)
	print(round(desconto, 2))
else:
	print(round(valor, 2))