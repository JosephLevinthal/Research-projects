compra = float(input("Preco da compra: "))

if (compra >= 200.00):
	desconto = compra*0.05
	mensagem = compra - desconto
else:
	mensagem = compra

print(round(mensagem, 2))	