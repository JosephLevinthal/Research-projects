var = input("quantos sucos ")
var2 = input("quantos salgados ")
dis = input("digite o seu saldo ")
total = (var * 3 + var2 * 3.5)

if dis >= total:
	mensagem = sim
else:
	mensagem = nao
	
print (round(total + mensagem, 2))