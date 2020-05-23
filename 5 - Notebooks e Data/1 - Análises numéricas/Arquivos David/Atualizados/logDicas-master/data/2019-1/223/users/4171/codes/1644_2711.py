valord = int(input("valor disponivel: "))
tickets = int(input("quantidade de tickets: "))
vtickets = float(input("valor dos tickets: "))
passes = int(input("quantidade de passes: "))
vpasses = float(input("valor dos passes: "))

if valord > tickets*vtickets + passes*vpasses:
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")