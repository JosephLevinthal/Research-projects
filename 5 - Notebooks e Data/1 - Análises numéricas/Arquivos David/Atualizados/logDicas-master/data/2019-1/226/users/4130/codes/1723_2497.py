x = float(input("Quantidade inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4.0
saldo = x # Variavel acumuladora

# Valor inicial da variavel contadora
t = tempo


while(t >= 1):
	renda = (saldo * juros) / 100
	saldo = saldo + renda
	t = t - 1
	print(round(saldo, 2))