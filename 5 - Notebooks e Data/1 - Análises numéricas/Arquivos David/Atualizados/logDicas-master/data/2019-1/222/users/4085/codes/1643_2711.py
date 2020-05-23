valortotal = float(input("escreva o valor total que ele possui: "))
qtdtickets = int(input("escreva a quantidade de tickets do RU que ele necessita: "))
valorticket = float(input("escreva o valor dos tickets: "))
qtdpasses = int(input("escreva a quantidade de passes que ele necessita: "))
valorpasse = float(input("escreva o valor do passe: "))
a = qtdtickets * valorticket
b = qtdpasses * valorpasse
if (valortotal >= a + b):
	mensagem = "SUFICIENTE"
else:
	mensagem = "INSUFICIENTE"
	
print(mensagem)