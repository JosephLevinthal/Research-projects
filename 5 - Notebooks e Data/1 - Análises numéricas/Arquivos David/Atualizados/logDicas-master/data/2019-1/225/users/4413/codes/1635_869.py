preco = float(input("produto: "))
if(preco>=200):
	mensagem = (preco - preco*5/100)
else: 
	mensagem = (preco)
print(round(mensagem, 2))