qi    = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4/100
saldo = qi      


t = 0

# Atualizacao de saldo
while (t < tempo):
	rend = (saldo * juros)
	saldo = saldo + rend
	t = t + 1
	print(round(saldo, 2)) # Exibicao de resultados

	
