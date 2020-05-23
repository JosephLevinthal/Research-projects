qi    = float(input("Quantia inicial: "))
tempo = int(input("q de meses de investimento: "))
juros = 0.04
saldo = qi      
t = 0 #(tempo)

while ( t < tempo):
	rend = saldo * 0.04
	saldo = saldo + rend
	t = t + 1
	print(round(saldo, 2)) 

	
