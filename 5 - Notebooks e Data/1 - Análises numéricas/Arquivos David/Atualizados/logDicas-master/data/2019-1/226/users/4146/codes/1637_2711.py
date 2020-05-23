valor = float(input("Digite o valor: "))
tickets = int(input("Digite a quatidade: "))
precoA = float(input("Digite o preco: "))
passe = int(input("Digite a quantidade: "))
precoB = float(input("Digite o preco: "))

gasto = (tickets*precoA) + (passe*precoB)

if (valor >= gasto):
	mensagem = "SUFICIENTE"
else:
	mensagem = "INSUFICIENTE"

print(mensagem)	