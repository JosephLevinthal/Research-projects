n = int(input("insira o numero:"))
x = 0
soma = 0
while(x < n):
	x = x + 1
	if(n % x == 0 and x != n):
		print(x)
		soma = soma + x
if(soma == n):
	print("PERFEITO")
else:
	print("NAO PERFEITO")
