din = float(input("digite seu orcamento: "))
RU = int(input("digite a quantidade que deseja de tickets: "))
tickets = float(input("valor do tickets: "))
passes = int(input("digite a quantidade de passes que deseja: "))
passagem = float(input("valor da passagem: "))
if (((RU*tickets)+(passes*passagem)) <= din):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")