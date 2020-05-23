# Instituto de Computacao - UFAM
# Lab 04 - Ex 04
# 20 / 06 / 2016

qi    = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4/100
saldo = qi      # Variavel acumuladora
t = 0 #acumula qtd. de meses
i= 1 #contadora
# Atualizacao de saldo
while (i <= tempo):
	i=i+1
	rend = (saldo * juros)
	saldo = saldo + rend
	t = t + 1
	print(round(saldo, 2)) # Exibicao de resultados

	
