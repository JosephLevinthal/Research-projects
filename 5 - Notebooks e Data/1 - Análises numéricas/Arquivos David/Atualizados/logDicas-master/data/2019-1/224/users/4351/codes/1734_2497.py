qi    = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4/100
saldo = qi      # Variavel acumuladora

# Valor inicial da variavel contadora
t = 0

# Atualizacao de saldo
while (t != tempo):
	rend = saldo * juros
	saldo = saldo + rend
	print(round(saldo, 2)) # Exibicao de resultados
	t = t + 1


