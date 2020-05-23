valor = float(input("valor inicial: "))
tickets = int(input("quantidade de tickets: "))
precoti = float(input("preco dos tickets: "))
passes = int(input("quantidade de passes: "))
precopass = float(input("preco dos passes: "))
if valor >= (tickets*precoti)+(passes*precopass):
	mensagem = "suficiente".upper()
else:
	mensagem = "insuficiente".upper()
print(mensagem)