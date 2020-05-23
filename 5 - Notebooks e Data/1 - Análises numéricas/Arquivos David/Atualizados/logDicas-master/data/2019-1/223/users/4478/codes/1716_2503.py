n = int(input("numero: "))
soma = 0
d = 1
cont = 0
sinal = 1
while(cont < n):
	soma = soma + (sinal*(4/d))
	sinal = sinal*(-1)
	d = d + 2
	cont = cont + 1
print(round(soma, 8))
