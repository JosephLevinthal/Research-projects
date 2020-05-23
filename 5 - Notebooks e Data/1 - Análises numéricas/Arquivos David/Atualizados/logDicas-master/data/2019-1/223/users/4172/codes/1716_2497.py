# Instituto de Computacao - UFAM
# Lab 04 - Ex 04
# 20 / 06 / 2016

qi    = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4.0
sald = qi      # Variavel acumuladora

# Valor inicial da variavel contadora
t = 0

# Atualizacao de saldo
while (t!=tempo):
	rend = (sald*juros)/100
	sald = sald  + rend
	t += 1
	print(round(sald, 2)) # Exibicao de resultados
