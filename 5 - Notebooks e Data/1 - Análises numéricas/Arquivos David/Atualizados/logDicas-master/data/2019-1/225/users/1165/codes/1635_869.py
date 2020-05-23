preco = float(input("Leia o preco sem esconto: "))

if (preco >= 200):
	mensagem = preco * 0.95
	
print(round(mensagem, 2))
