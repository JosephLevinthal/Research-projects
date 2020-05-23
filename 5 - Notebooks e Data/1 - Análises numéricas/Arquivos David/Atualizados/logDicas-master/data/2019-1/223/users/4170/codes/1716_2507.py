qi = int(input("Quantidade inicial: "))
p = int(input("Percentual de crescimento: "))
percentual = p/ 100
limite = 8000
t = 0
while(qi>0 and qi<limite):
	qm = int(input("Quantidade mensal de retirados: "))
	qi = qi - qm + (qi * percentual)
	t = t + 1
	if(qi>=limite):
		x = "MAXIMO"
	else:
		x = "ZERO"
print(x)
print(t)