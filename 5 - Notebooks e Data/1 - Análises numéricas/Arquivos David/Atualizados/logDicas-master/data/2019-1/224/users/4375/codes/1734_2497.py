qi    = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4.0/100
saldo = qi     
t = 0
while (t!=tempo):
	rend = saldo * juros
	saldo = saldo + rend
	print(round(saldo, 2))
	t=t+1


	
