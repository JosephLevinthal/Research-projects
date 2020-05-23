n = int(input())

contador = 1
divisor = -1
soma = 0
while( contador <= n):
	contador = contador + 1
	divisor = divisor + 2
	soma = soma + ((-1)** contador) * (4/ divisor)
	
print(round(soma , 8))