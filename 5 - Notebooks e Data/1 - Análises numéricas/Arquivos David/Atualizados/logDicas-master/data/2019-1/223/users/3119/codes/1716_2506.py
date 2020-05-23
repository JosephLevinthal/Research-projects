inicio = int(input("Quantidade inicial: "))
perc = int(input("Digite o percentual de crescimento: "))
quant = int(input("Digite a quantidade retirada: "))

p = perc/100
limite = 12000
t = 0

while(inicio > 0 and inicio < limite):
	inicio = inicio - quant + (inicio * p)
	t = t + 1
	if(inicio >= limite):
		x = "LIMITE"
	else:
		x = "EXTINCAO"
print(x)
print(t)
	