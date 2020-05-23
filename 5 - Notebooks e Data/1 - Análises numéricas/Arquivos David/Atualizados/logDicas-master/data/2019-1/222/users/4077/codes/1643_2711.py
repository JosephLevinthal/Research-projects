var = float(input("var disponivel: "))
tickets = int(input("quantidade: "))
vart = float(input("var tickets: "))
passes = int(input("passes: "))
varp = float(input("var passes: "))
soma = tickets * vart + passes * varp
if(var >= soma):
	print("SUFICICENTE")
else:
	print("INSUFICIENTE")
	