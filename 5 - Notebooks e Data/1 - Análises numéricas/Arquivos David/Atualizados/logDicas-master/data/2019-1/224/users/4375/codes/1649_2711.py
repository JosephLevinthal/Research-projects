v = float(input("Valor: "))
qTru = int(input("Quantidade de Tickets do RU: "))
vT = float(input("Valor dos Tickets: "))
qPo = int(input("Quantidade de passes de onibus: "))
vP = float(input("Valor dos passes: "))
operacao = ((qTru * vT) + (qPo * vP))
if(v >= operacao):
	mensagem = " SUFICIENTE"
	print(mensagem)
else:
	mensagem = " INSUFICIENTE"
	print(mensagem)
	