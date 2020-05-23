valor = float(input("valor: "))
tickets_ru = int(input("quantidade de tickets do RU: "))
valor_ticket = float(input("valor dos tickets: "))
passe_bus = int(input("quantidade de passes de onibus: "))
valor_bus = float(input("valor dos passes: "))

if valor >= (tickets_ru * valor_ticket) + (passe_bus * valor_bus):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")