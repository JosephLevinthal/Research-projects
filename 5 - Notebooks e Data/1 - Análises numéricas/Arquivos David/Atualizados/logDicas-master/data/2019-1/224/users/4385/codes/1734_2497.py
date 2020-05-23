qi    = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4.0
saldo = qi      

t = 0

while (t < tempo):
	rend = saldo * juros/100
	saldo = saldo + rend
	t = t + 1

	print(round(saldo, 2)) 

	
