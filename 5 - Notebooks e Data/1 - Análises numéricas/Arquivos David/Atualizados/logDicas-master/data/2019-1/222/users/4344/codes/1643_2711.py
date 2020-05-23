valor = float(input("Valor disponivel: "))
qtd_ticketsRU = int(input("Quantos tickets deseja comprar? "))
valor_ticketsRU = float(input("Valor do tickets: "))
qtd_passesBus = int(input("Quantos passes deseja? "))
valor_passesBus = float(input("Valor dos passes: "))

somatorio = qtd_ticketsRU*valor_ticketsRU + qtd_passesBus*valor_passesBus

if valor >= somatorio:
	print("SUFICIENTE")
elif valor < somatorio:
	print("INSUFICIENTE")