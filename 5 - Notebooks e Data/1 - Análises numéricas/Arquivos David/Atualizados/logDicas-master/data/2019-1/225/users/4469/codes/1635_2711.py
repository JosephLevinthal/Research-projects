valor_disponivel = float(input("Quanto disponivel? "))
qtde_tickets = int(input("Quantos tickets ira comprar? "))
valor_ticket = float(input("Quanto custa um ticket? "))
qtde_passes = int(input("Quantos passes ira comprar? "))
valor_passe = float(input("Quanto custa um passe? "))

total_compra = (qtde_tickets * valor_ticket) + (qtde_passes * valor_passe)

if(valor_disponivel >= total_compra):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")