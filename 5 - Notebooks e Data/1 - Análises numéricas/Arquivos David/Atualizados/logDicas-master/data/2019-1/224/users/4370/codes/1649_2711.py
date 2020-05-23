valor_disponivel = float(input("valor disponivel: "))
qtd_tickets = int(input("quantidade de tickets: "))
valor_ticket = float(input("valor do ticket "))
qtd_passe_onibus = int(input("quantidade dos passes: "))
valor_passes = float(input("valor do passe: "))

valor_total_ticket = valor_ticket * qtd_tickets
valor_total_passe = valor_passes * qtd_passe_onibus
if(valor_disponivel > valor_total_ticket + valor_total_passe) :
	print("SUFICIENTE")
else :
	print("INSUFICIENTE")