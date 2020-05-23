valor = float(input("Valor Disponivel: "))
qtRU = int(input("Tickets do RU: "))
Vtickets = float(input("Valor dos Tickets: "))
QPbus = int(input("Quantidade de passes de onibus:"))
Vpasses = float(input("Valor dos passes: "))
if (valor >= (qtRU *Vtickets)+ (QPbus*Vpasses)):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")