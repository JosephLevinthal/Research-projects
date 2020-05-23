# Instituto de Computacao - UFAM
# Lab 04 - Ex 04
# 20 / 06 / 2016

qi    = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4.0
saldo = qi      # Variavel acumuladora

# Valor inicial da variavel contadora
t = 0 #acumula o tempo transcorrido em meses

# Atualizacao de saldo
while (t>=0 and t< tempo): #Condicao do laco: o tempo comeca com 0 meses e eh repetido ate q o tempo total da aplicacao termine
	rend = saldo * juros/100 #calculo do rendimento: saldo anterior multiplicado pela taxa de juros
	saldo = saldo + rend # atualizacao do saldo
	t = t + 1 #contagem dos meses
	
	print(round(saldo, 2)) # Exibicao de resultados

	
