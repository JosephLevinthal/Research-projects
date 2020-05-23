Valor=float(input("valor disponivel:"))
b=int(input("quantidades de tickets do RU:"))
c=float(input("valor dos tickets:"))
d=int(input("quantidades de passes:"))
e=float(input("valor dos passes:"))
soma=(b*c)+(d*e)
if(Valor>=soma):
	mensagem="SUFICIENTE"
	print(mensagem)
else:
	mensagem="INSUFICIENTE"
	print(mensagem)