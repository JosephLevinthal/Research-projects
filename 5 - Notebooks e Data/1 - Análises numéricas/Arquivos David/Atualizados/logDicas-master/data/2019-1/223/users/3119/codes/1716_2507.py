inicio = int(input("Quantidade inicial: "))
perc = int(input("Digite o percentual de crescimento: "))

p = perc/100
limite = 8000
t = 0

while(inicio > 0 and inicio < limite):
	venda = int(input("Digite a quantidade retirada: "))
	inicio = inicio - venda + (inicio * p)
	t = t + 1
	if(inicio >= limite):
		x = "MAXIMO"
	else:
		x = "ZERO"
print(x)
print(t)
	