preco = float(input("digite preco: "))
pag = float(input("digite pag: "))

if(preco > pag):
	valor = preco - pag
	mensagem = ("Falta ")+ str(round(valor, 2)) 
else:
	valor = pag - preco
	mensagem = ("Troco de ")+ str(round(valor, 2))

print(mensagem)