# Instituto de Computacao - UFAM
# Lab 04 - Ex 04
# 20 / 06 / 2016

qi = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 0.04
saldo = qi      


# Valor inicial da variavel contadora
t = 0

# Atualizacao de saldo
while (tempo>=0 and t<tempo):
	rend = saldo* juros
	saldo = saldo + rend
	t = t+1

	print(round(saldo, 2)) # Exibicao de resultados
