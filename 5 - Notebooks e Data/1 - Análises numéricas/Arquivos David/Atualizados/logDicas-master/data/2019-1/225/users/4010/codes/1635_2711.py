valor = float(input("valor: "))
quantru = int(input("quant: "))
valorru = float(input("valor do r.u: "))
quantpasse = int(input("quant: "))
valorpasse = float(input("valor do passe: "))
total = float(quantru*valorru + quantpasse*valorpasse)

if(valor >= total):
	mensagem = "SUFICIENTE"
	print(mensagem)
else:
	mensagem = "INSUFICIENTE"
	print(mensagem)