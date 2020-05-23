N = int(input("insira o numero de termos: "))

valor = 1
soma = 1
cont = 1

while(cont <= N):
	soma = soma * (cont/(cont*2+1))
	valor = soma + valor
	cont += 1

print(round(2*valor,10))