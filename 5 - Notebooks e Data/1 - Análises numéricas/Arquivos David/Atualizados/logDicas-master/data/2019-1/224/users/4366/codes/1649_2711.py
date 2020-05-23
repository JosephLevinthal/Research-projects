valor=int(input("digite o valor disponivel:"))
RU=int(input("digite a quantidade de tickets do RU:"))
tickets=float(input("digite o valor dos tickets:"))
passes=int(input("digite a quantidade de passes de onibus:"))
busao=float(input("digite o valor dos passes:"))
if(tickets*RU+passes*busao<=valor):
	mensagem="SUFICIENTE"
	print(mensagem.upper())
else:
	mensagem="INSUFICIENTE"
	print(mensagem.upper())