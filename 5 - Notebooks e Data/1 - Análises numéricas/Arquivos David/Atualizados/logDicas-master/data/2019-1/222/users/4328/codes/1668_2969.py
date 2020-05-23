
quantidade = int(input())
preco1 = float(input())
preco2 = float(input())

if (quantidade >= 2):
	valor = (preco1 + (0.75 * preco2))
else:
	valor = (preco1)
	
print(round(valor,2))
