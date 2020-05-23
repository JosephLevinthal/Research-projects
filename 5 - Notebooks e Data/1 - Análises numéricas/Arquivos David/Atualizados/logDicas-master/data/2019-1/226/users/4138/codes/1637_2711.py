V = float(input("insira o valor: "))
Q = int(input("quantidade de tickets: "))
vt = float(input("valor dos tickets"))
po = float(input("quantidade de passes de onibus: "))
vpo = float(input("valor dos passes: "))

T = Q * vt
O = po * vpo

tot = T + O
if( V > tot):
	mensagem = "SUFICIENTE"
else:
	mensagem = "INSUFICIENTE"
	
print(mensagem)