valor=float(input("valor:"))
quantru=int(input("quantidade:"))
valorru=float(input("ru:"))
quantpasse=int(input("qp:"))
valorpasse=float(input("valor passe :"))
total=float(quantru*valorru + quantpasse*valorpasse)

if(valor >=total):
	mensagem = "SUFICIENTE"
	print(mensagem)
else:
	mensagem = "INSUFICIENTE"
	print(mensagem)