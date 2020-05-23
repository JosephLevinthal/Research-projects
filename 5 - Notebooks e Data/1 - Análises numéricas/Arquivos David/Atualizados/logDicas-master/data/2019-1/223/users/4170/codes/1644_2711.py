money = float(input("a:"))
quantru = int(input("aa:"))
ticket = float(input("aaa:"))
quantpasse = int(input("aaaa:"))
passe = float(input("aaaaa:"))

total = (quantru * ticket) + (quantpasse * passe)

if (total < money):
	mensagem = "SUFICIENTE"
	print(mensagem)
else:
	mensagem = "INSUFICIENTE"
	print(mensagem)