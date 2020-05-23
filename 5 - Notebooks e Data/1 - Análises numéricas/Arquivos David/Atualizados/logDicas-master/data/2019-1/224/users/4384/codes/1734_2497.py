qi = int(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4.0
saldo = qi     


t = 0

while (tempo<12):
	rend = saldo * juros
	saldo = saldo + (rend/100)
	t = t+1
print(round(saldo, 2)) 

	
