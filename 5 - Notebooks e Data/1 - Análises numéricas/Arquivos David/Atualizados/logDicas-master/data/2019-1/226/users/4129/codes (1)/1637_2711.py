valor = float(input("Valor disponivel:"))
tickets = int(input("Quantidade de ticktes:"))
valortick = float(input("valor dos tickets:"))
passes = int(input("Quantidade de passes:"))
valorpass = float(input("valor dos passes:"))
if(valor >= (tickets*valortick)+(passes*valorpass)):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")