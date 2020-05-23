valor = float(input("Valor disponivel: "))
quantidade = int(input("Quantidade de tickets: "))
valor_tickets = float(input("Valor dos tickets: "))
quantidade_onibus = int(input("Quantidade de passes de onibus: "))
valor_passes = float(input("Valor dos passes: "))

if (valor > quantidade):
	mensagem = "suficiente"
else:
	mensagem = "insuficiente"

print(mensagem)