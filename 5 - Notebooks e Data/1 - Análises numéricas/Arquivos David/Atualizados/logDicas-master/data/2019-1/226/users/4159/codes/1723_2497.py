qi    = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 0.04
saldo = qi     
t = 0
while (tempo>t):
	rend = saldo * juros
	saldo = saldo + rend
	t = t+1
	print(round(saldo, 2)) 

	
