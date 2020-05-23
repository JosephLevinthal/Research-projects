Saldo = float(input("saldo: "))
RU = int(input("quantidade de tickets: "))
vt = float(input("valor: "))
qp = int(input("passes: "))
vp = float(input("valor: "))
eq = (RU*vt) + (qp*vp)
if(Saldo >= eq):
	mensagem = "SUFICIENTE"
else:
	mensagem = "INSUFICIENTE"
print(mensagem)