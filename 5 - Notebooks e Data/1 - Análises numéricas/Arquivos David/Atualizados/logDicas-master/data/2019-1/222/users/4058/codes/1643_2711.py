valor = float(input("dinheiro inicial: "))
tickets = int(input("quantidade: "))
valortick = float(input("valor: "))
passes = int(input("quantidade: "))
valorpass = float(input("valor: "))
if valor >= (tickets*valortick) + (passes*valorpass):
	mensagem = "suficiente"
else:
	mensagem = "insuficiente"
print(mensagem.upper())