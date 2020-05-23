valor = float(input("o valor que ele tem disponivel: "))
tickets= int(input("a quantidade de tickets do ru que ele deseja comprar: "))
valor_tickets =float(input("o valor dos tickets: "))
passes =float(input("a quantidade de passes de onibus: "))
valor_dos_passses =float(input("o valor dos passes: "))
if(valor >= (tickets * valor_tickets + passes * valor_dos_passes)):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
