# Instituto de Computacao - UFAM
# Lab 04 - Ex 04
# 20 / 06 / 2016

qi    = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4.0
saldo = qi      # Variavel acumuladora

# Valor inicial da variavel contadora
t = 0

# Atualizacao de saldo
while (t< tempo):
	rend = (saldo*juros)/100
	saldo = saldo + rend
	t= t+1
	y= round(saldo,2)
	print(y) # Exibicao de resultados

	
