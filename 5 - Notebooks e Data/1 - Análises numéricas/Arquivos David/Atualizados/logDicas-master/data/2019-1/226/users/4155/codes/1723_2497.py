qi = float(input("valor: "))
tempo = int(input("quantidade: "))
juros = 4.0
saldo = qi      # Variavel acumuladora

t = 0
# Atualizacao de saldo
while (tempo > 1 and t < tempo):
	rend = saldo * (juros /100)
	saldo = saldo + rend
	t = t + 1
	print(round(saldo, 2))