valor = float(input("Valor disponivel: "))
ticketQtde = int(input("Quantidade de Ticket: "))
ticketValor = float(input("Valor do Ticket: "))
passeQtde = int(input("Quantidade de passes de onibus: "))
passeValor = float(input("Valor da passagem: "))

ticket = ticketQtde * ticketValor
passagem = passeQtde * passeValor
total = ticket + passagem

if total <= valor:
	mensagem = "Suficiente"
else:
	mensagem = "Insuficiente"
	
print (mensagem.upper())