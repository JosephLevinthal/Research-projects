valor = float(input("valor disponivel: "))
tickets = int(input("quantidade de tickets do RU: "))
valor_tickets = float(input("valor unitario dos tickets: "))
passes = int(input("quantidades de passes: "))
valor_dos_passes = float(input("valor unitario dos passes: "))

if(valor >= (tickets * valor_tickets + passes * valor_dos_passes)):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")