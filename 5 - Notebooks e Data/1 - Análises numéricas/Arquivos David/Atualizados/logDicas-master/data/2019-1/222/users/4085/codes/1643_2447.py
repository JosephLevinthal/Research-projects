pc = float(input("escreva o valor do preco: "))
pg = float(input("escreva o valor do pagamento: "))

if (pc > pg):
	mensagem = "Falta " 
	valor = pc - pg
else:
	mensagem = "Troco de " 
	valor = pg - pc

print(mensagem, round(valor, 2))