# Instituto de Computacao - UFAM
# Lab 04 - Ex 04
# 20 / 06 / 2016

qi    = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 0.04
saldo = qi      # Variavel acumuladora

# Valor inicial da variavel contadora
t = 0
i = 1

# Atualizacao de saldo
while (i <= tempo):
	i = i + 1
	renda = saldo * (juros)
	saldo = saldo + renda
	print(round(saldo, 2)) # Exibicao de resultados

	
