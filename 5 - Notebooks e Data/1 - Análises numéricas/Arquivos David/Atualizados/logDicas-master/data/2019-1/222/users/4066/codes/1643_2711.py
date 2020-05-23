valor = float(input("valor disponivel: "))
tickets = int(input("tickets: "))
vt = float(input('valor dos ticket: '))
passes = int(input('passes: '))
vp = float(input('valor dos passes: '))

total = tickets*vt + passes*vp

if (valor > total):
	print("SUFICIENTE")
	
else:
	print("INSUFICIENTE")