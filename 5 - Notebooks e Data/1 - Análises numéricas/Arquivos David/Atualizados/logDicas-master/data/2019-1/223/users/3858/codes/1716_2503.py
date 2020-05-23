n = int(input())
soma = 0
a = 1
v = 0
sinal = 1

while(v<n):
	soma = (soma + sinal*(4/a))
	sinal = sinal * (-1)
	a = a + 2
	v = v + 1 
	
print(round(soma,8))