preco = float(input("preco: "))
pag = float(input("pag: "))
x = float(preco - pag)
y = float(pag - preco)

if(preco > pag):
	mensagem = "Falta "
	print(mensagem, (round(x, 2)))
else:
	mensagem = "Troco de "
	print(mensagem, (round(y, 2)))