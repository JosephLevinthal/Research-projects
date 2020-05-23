q_inicial = int(input("quantidade inicial: "))
perc = float(input("percentual de crescimento: "))
quant = int(input("quantidade de pirarucus retirados: "))
perc = perc/100
t = 0
while(0 <= q_inicial <= 12000):
	q_inicial = (q_inicial + q_inicial * perc) - quant
	t = t + 1
if(q_inicial <= 0):
	print("EXTINCAO")
	print(t)
if(q_inicial >= 12000):
	print("LIMITE")
	print(t)
