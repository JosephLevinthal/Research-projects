preco = float(input("Digite um numero: "))
pag = float(input("Digite um numero: "))

if(preco>pag):
	x = preco-pag
	round(x, 2)
	mensagem="Falta "
else:
	x = pag-preco 
	round(x, 2)
	mensagem="Troco de "
	
print(mensagem,x)
	
