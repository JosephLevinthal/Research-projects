from math import * #importa as funcoes do math
#Entrada dos dados:
n = int(input("Digite um numero: "))
i = 0 #variavel contadora dos termos
soma = 0 #variavel acumuladora dos termos
while (i < n):
	nu = (-1)**i #para um termo, i = 0, n = -1**0 = 1 e d =1, logo n/d = 1
	#para 2 termos, i = 1, o segundo termo sera negativo. De 3 termos em diante o sinal sera alternado
	d = (2*i + 1)*3**i
	soma = soma + (nu/d)
	i = i + 1
	print(n)
	print(d)
	print(n/d)
pi = soma*12**0.5
print(round(pi, 8))