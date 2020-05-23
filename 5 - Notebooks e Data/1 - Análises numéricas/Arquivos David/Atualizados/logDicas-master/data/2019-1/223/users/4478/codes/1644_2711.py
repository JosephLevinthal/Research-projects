valor = float(input("dinheiros: "))
RU = int(input("quantidade de tickets: "))
tickets = float(input("valor do tickets: "))
passe = int(input("quantidade de passes: "))
bus = float(input("valor da passagem estudantil: "))
total = RU*tickets+passe*bus
if(total<=valor):
	mensagem = "suficiente"
else:
	mensagem = "insuficiente"
print(mensagem.upper())