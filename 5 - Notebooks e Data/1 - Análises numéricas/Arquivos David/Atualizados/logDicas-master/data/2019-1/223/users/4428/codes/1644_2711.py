valor_disponivel = float(input("Digite o valor disponivel: "))
quantidade_tickets = int(input("Digite a quantidade de tickets: "))
valor_tickets = float(input("Digite o valor dos tickets: "))
quantidade_passes = int(input("Digite a quantidade de passes: "))
valor_passes = float(input("Digite o valor dos passes: "))

gasto_tickets = quantidade_tickets*valor_tickets
gasto_passes = quantidade_passes*valor_passes
gasto_total =  gasto_tickets + gasto_passes

if(valor_disponivel > gasto_total):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
