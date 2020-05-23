# Instituto de Computacao - UFAM
# Lab 04 - Ex 04
# 20 / 06 / 2016

qi = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4.0
saldo = qi      # Variavel acumuladora

# Valor inicial da variavel contadora
t = 0
renda=0
# Atualizacao de saldo
while (t<tempo):
	renda = saldo * (juros/100)
	saldo = saldo + renda
	t = 1 + t
	print(round(saldo, 2)) # Exibicao de resultados
	
