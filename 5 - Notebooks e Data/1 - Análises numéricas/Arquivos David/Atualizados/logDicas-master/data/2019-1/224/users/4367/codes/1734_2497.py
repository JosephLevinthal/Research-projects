qi    = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4.0/100
saldo = qi      # Variavel acumuladora

# Valor inicial da variavel contadora
t = 0

# Atualizacao de saldo
while (tempo>t):
	rend = saldo * juros
	saldo = saldo + rend
	t = t+1
	print(round(saldo, 2)) # Exibicao de resultados
