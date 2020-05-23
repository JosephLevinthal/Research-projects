total=float(input("dinheiro do brother: "))
qtd_ticket_ru=int(input("qtd de tickets do RU: "))
valor_ticket_ru=float(input("valor do ticket: "))
qtd_busao=int(input("qtd de passes de onibus: "))
valor_passes=float(input("valor do passe: "))
x=(qtd_ticket_ru*valor_ticket_ru)+(qtd_busao*valor_passes)
if (total>=x):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")